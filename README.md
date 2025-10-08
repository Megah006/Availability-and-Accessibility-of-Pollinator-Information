This readme.txt file was generated on 20251007 by Omar Megahed  
Recommended citation for the data:  
Megahed, Omar; DiGiacomo, Gigi; Wimmer, Madeline; Schuh, Marissa (2025). Information as an Ecological Driver: Availability and Accessibility of Pollinator Information for Specialty Crop Systems in the U.S. Midwest. University of Minnesota Digital Conservancy (DRUM).


-------------------
GENERAL INFORMATION
-------------------

1. Title of Dataset  
Information as an Ecological Driver: Availability and Accessibility of Pollinator Information for Specialty Crop Systems in the U.S. Midwest  

2. Author Information  

  Principal Investigator Contact Information  
        Name: Gigi DiGiacomo  
        Institution: University of Minnesota  
        Address:  Department of Applied Economics, 146 Ruttan Hall, 1994 Buford Avenue, Saint Paul, MN 55108
        Email: gigid@umn.edu 
        ORCID: N/A  

  Associate or Co-investigator Contact Information  
        Name: Omar Megahed  
        Institution: University of Minnesota  
        Address: N/A
        Email: mega006@umn.edu  
        ORCID: N/A  

  Associate or Co-investigator Contact Information  
        Name: Madeline Wimmer  
        Institution: University of Minnesota Extension
        Address: N/A
        Email: wimm0035@umn.edu
        ORCID: N/A  

  Associate or Co-investigator Contact Information  
        Name: Marissa Schuh  
        Institution: University of Minnesota Extension  
        Address: N/A
        Email: mschuh@umn.edu
        ORCID: N/A  

3. Date published or finalized for release: 2025-10-07  

4. Date of data collection: 2024 to 2025-08  

5. Geographic location of data collection:  
U.S. Midwest (Minnesota, Wisconsin, Iowa, Illinois, Michigan, Indiana, Ohio)  

6. Funding sources:  
University of Minnesota College of Food, Agriculture and Natural Resource Sciences, project #1806-11033-FAPOL-1377051.

7. Overview of the data (abstract):  
This dataset and Python code are analysis of pollinator outreach materials evaluated using a resource discoverability rubric. The data represent rubric-based scores across multiple media types (Extension articles, academic papers, multimedia resources, and more), which assess Accessibility, Metadata quality, Search Engine Visibility, Sharability, and Indexing. The script aggregates rubric results by article type and produces a summary of the statistics. 


--------------------------
SHARING/ACCESS INFORMATION
--------------------------

1. Licenses/restrictions placed on the data:    
This dataset and accompanying code are released under the **Creative Commons Zero (CC0 1.0 Universal)** Public Domain Dedication.  
By applying CC0, the authors waive all rights to the data and make it freely available for reuse without restriction.  
Users may copy, modify, distribute, and use the data and scripts for any purpose without needing to request permission.  
For details, see: https://creativecommons.org/publicdomain/zero/1.0/


2. Links to publications that cite or use the data:  
Manuscript in preparation for submission to *Basic and Applied Ecology*.  

3. Was data derived from another source?  
No, primary data collected and compiled by the project team.  

4. Terms of Use:  
Data Repository for the University of Minnesota (DRUM). By using these files, users agree to the Terms of Use:  
https://conservancy.umn.edu/pages/policies/#drum-terms-of-use  

---------------------
DATA & FILE OVERVIEW
---------------------

1. File List  

   A. Filename: `aggregate.py`  
      Short description: Python script used to aggregate rubric scores by article type and compute statistics.  

   B. Filename: `Copy of Updated Grading Discoverability_ Advancing Adoption of Integrated Pest and Pollinator Management in the Midwest - Sheet1.csv`  
      Short description: Dataset containing final rubric-based scores for evaluated resources, including article type and scoring categories.  

   C. Filename: `README.md`  
      Short description: Descriptive documentation for the GitHub repository and script usage.  

2. Relationship between files:  
`aggregate.py` reads the input CSV file, performs data cleaning and grouping, and exports results as `aggregated_scores_by_article_type.csv`.  


--------------------------
METHODOLOGICAL INFORMATION
--------------------------

1. Description of methods used for collection/generation of data:  
Resources were identified through an environmental scan of Extension, nonprofit, and academic sources. Each resource was graded by an evaluator using a standardized rubric used for assessing discoverability criteria.  

2. Methods for processing the data:  
The `aggregate.py` script groups the rubric scores by article type and calculates summary statistics (mean, median, min, max, range) for each scoring category. Results are rounded and exported as a CSV.  

3. Instrument- or software-specific information:  
Developed in Python 3.13 using the pandas library (version 2.3.1).  

4. Standards and calibration information:  
A single evaluator conducted all scoring using consistent rubric criteria.

6. Environmental/experimental conditions:  
N/A  

7. Quality-assurance procedures:  
Data were reviewed for missing or out-of-range scores and verified through manual spot-checking before analysis.  

8. People involved with sample collection, processing, analysis, and/or submission:  
Gigi DiGiacomo – Principal Investigator  
Omar Megahed – Data processing, code development, analysis, and submission  
Madeline Wimmer – Data collection and grading  
Marissa Schuh – Data collection and review guidance  


-----------------------------------------
DATA-SPECIFIC INFORMATION FOR: Copy of Updated Grading Discoverability_ Advancing Adoption of Integrated Pest and Pollinator Management in the Midwest - Sheet1.csv
-----------------------------------------

1. Number of variables: 8
 
2. Number of cases/rows: 1015 (varies by dataset version)  

3. Missing data codes:  
        NaN — no score assigned or not applicable  

4. Variable List:  

-----------------------------------------
DATA-SPECIFIC INFORMATION FOR: Copy of Updated Grading Discoverability_ Advancing Adoption of Integrated Pest and Pollinator Management in the Midwest - Sheet1.csv
-----------------------------------------

1. Number of variables: 12  
2. Number of cases/rows: 100+ (varies by dataset version)  

3. Missing data codes:  
        NaN — no score assigned or not applicable  

4. Variable List:  

    A. Name: Article Name  
       Description: Title of the resource evaluated using the rubric.  

    B. Name: Accessibility Score  
       Description: Numeric score indicating the ease of access and usability for the audience.  

    C. Name: Metadata Score  
       Description: Numeric score indicating the completeness, accuracy, and structure of metadata associated with the resource.  

    D. Name: Search Engine Visibility Score  
       Description: Numeric score indicating how easily the resource can be found via standard web searches.  

    E. Name: Sharability Score  
       Description: Numeric score indicating how easily the resource can be shared through links or social media.  

    F. Name: Indexing Score  
       Description: Numeric score indicating whether the resource appears in relevant databases or indexes.  

    G. Name: Overall Score  
       Description: Combined weighted mean of all rubric categories, representing total discoverability performance.  

    H. Name: Website Link  
       Description: URL link to the evaluated resource.  

    I. Name: Article Type  
       Description: Type or format of the resource (e.g., Extension article, research publication, fact sheet, video).  

    J. Name: Source  
       Description: Organization, publisher, or institution that produced the resource.  

    K. Name: Year  
       Description: Year of publication or last update of the resource.  

    L. Name: Keywords Used  
       Description: Search keywords used to locate and identify the resource during the environmental scan.
   
Format of the README.md is from http://z.umn.edu/readme
