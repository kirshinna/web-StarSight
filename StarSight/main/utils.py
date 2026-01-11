import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
import base64

def filter_night_hours(day):
    night_hours = []
    for h in day.get("hours", []):
        hour = int(h["datetime"].split(":")[0])
        if hour >= 21 or hour <= 3:
            night_hours.append(h)
    return night_hours

def calculate_hourly_scores(day):
    night_hours = filter_night_hours(day)
    for h in night_hours:
        h["score"] = calculate_observation_score(h)
    return night_hours

def prepare_heatmap_matrix(days):
    matrix = []
    row_labels = []

    for day in days:
        night_hours = calculate_hourly_scores(day)
        row_labels.append(day["datetime"])

        scores = []
        hours_order = [21,22,23,0,1,2,3]
        hour_map = {int(h["datetime"].split(":")[0]): h["score"] for h in night_hours}
        for hr in hours_order:
            scores.append(hour_map.get(hr, 0))
        matrix.append(scores)

    return pd.DataFrame(matrix, index=row_labels, columns=[str(h)+":00" for h in hours_order])


def generate_hourly_heatmap(df):
    plt.figure(figsize=(10, len(df) * 0.5))

    ax = sns.heatmap(df, cmap="YlGnBu", annot=True, fmt="d", cbar=True,
                     linewidths=0.5, linecolor="gray")

    plt.gcf().patch.set_alpha(0)
    ax.set_facecolor("none")

    ax.set_xlabel("Час ночи", color="white", fontsize=14)
    ax.set_ylabel("Дата", color="white", fontsize=14)

    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format="png", transparent=True)
    plt.close()
    buffer.seek(0)

    img_str = base64.b64encode(buffer.read()).decode("utf-8")
    return img_str

def calculate_observation_score(day):
    clouds = day.get("cloudcover", 100)
    moon = day.get("moonphase", 0.5)
    visible = day.get("visibility", 5)
    humidity = day.get("humidity", 50)

    K_transp = 0.7 + (visible / 20) - (humidity / 400)
    k_clouds = 1 - (clouds / 100)**1.5
    k_moon = 1 - (moon * 0.6)

    score = 100 * K_transp * k_clouds * k_moon

    if score < 0:
        score = 0
    if score > 100:
        score = 100

    return int(score)
