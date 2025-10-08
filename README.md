# Information as an Ecological Driver  

This repository contains Python scripts developed for the article  
*"Information as an Ecological Driver: Availability and Accessibility of Pollinator Information for Specialty Crop Systems in the U.S. Midwest."*  
The scripts are used to process and analyze scoring data from the resource discoverability rubric applied across different article types.

## Script: Aggregate Scores by Article Type  

This script reads in the graded dataset and groups results by **Article Type**. For each scoring category, it calculates summary statistics including the mean, median, minimum, maximum, and range. The output is a  CSV file (`aggregated_scores_by_article_type.csv`) that makes it easier to compare performance across categories. All numeric data is cleaned and rounded for readability.  

The scoring categories include: Accessibility, Metadata, Search Engine Visibility, Shareability, Indexing, and the Overall Score.  

## Dataset: “Copy of Updated Grading Discoverability_ Advancing Adoption of Integrated Pest and Pollinator Management in the Midwest - Sheet1.csv”

This file contains the finalized grading results from the resource discoverability rubric applied to outreach and research articles/materials. It serves as the **primary dataset** for testing and validating the aggregation script. Each entry represents a unique resource, with associated scores for all rubric categories.
