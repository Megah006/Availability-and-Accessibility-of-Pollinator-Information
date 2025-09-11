# Simple script to aggregate scores by article type
import pandas as pd

# File paths
input_csv = "Copy of Updated Grading Discoverability_ Advancing Adoption of Integrated Pest and Pollinator Management in the Midwest - Sheet1.csv"
output_csv = "aggregated_scores_by_article_type.csv"

# Column names
group_column = "Article Type"
score_columns = [
    "Accessibility Score",
    "Metadata Score",
    "Search Engine Visibility Score",
    "Sharability Score",
    "Indexing Score",
    "Overall Score",
]

# Read the data
data = pd.read_csv(input_csv)

# Convert score columns to numeric (in case of bad data)
for col in score_columns:
    data[col] = pd.to_numeric(data[col], errors="coerce")

# Prepare results
all_results = []
for score in score_columns:
    # Group by article type and calculate stats
    grouped = data.groupby(group_column)[score].agg(["mean", "median", "min", "max"]).reset_index()
    grouped["range"] = grouped["max"] - grouped["min"]
    # Add a column for the score name
    grouped.insert(0, "Section", score.replace(" Score", ""))
    all_results.append(grouped)

# Combine all results
final = pd.concat(all_results, ignore_index=True)

# Round numbers for easier reading
for stat in ["mean", "median", "min", "max", "range"]:
    final[stat] = final[stat].round(3)

# Save to CSV
final.to_csv(output_csv, index=False)
print(f"Saved: {output_csv}")
