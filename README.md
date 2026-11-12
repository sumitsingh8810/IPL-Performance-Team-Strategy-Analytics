# IPL Performance & Team Strategy Analytics

# 🏏 IPL Performance & Team Strategy Analytics | SQL & Power BI

## 📌 Project Overview

The **IPL Performance & Team Strategy Analytics** project is an end-to-end cricket data analytics project focused on analyzing Indian Premier League (IPL) matches, team performance, player statistics, and match strategies.

Using **MySQL** for data analysis and **Power BI** for interactive visualization, this project explores match outcomes, team wins, batting and bowling performance, toss decisions, and the impact of batting first versus chasing.

The dashboard provides an interactive way to explore IPL performance across the **2020–2025 seasons**.

## 🎯 Project Objectives

- Analyze overall IPL match statistics and season-wise performance.
- Compare team wins, losses, and win percentages.
- Evaluate team performance across different seasons.
- Identify top-performing batters and bowlers.
- Analyze batting and bowling statistics.
- Understand the relationship between toss decisions and match results.
- Compare batting first versus chasing performance.
- Explore head-to-head team comparisons.
- Build an interactive four-page Power BI dashboard.

## 📊 Dataset Overview

| Metric                   |   Details |
| ------------------------ | --------: |
| Seasons Covered          | 2020–2025 |
| Total Matches            |       444 |
| Total Deliveries         |    35,520 |
| IPL Teams                |        10 |
| Power BI Dashboard Pages |         4 |

### Dataset Tables

The project uses two cleaned datasets:

**1. `ipl_matches_cleaned_data`**

Contains match-level information used to analyze:

- Match details and seasons
- Participating teams
- Match winners
- Toss winners and toss decisions
- Match results
- Venues

**2. `ipl_deliveries_2020_2025_cleaned_data`**

Contains ball-by-ball information used to analyze:

- Batting and bowling performance
- Runs scored
- Wickets
- Boundaries
- Dot balls
- Player statistics

## 🛠️ Tools & Technologies

| Technology  | Application                             |
| ----------- | --------------------------------------- |
| MySQL       | Data querying and analysis              |
| SQL         | Data exploration and analytical queries |
| Power BI    | Interactive dashboard development       |
| DAX         | Measures, KPIs, and calculations        |
| Power Query | Data transformation and preparation     |
| CSV         | Dataset storage and management          |

## 🔄 Project Workflow

### 1. Data Understanding & Preparation

- Worked with match-level and ball-by-ball IPL datasets.
- Explored the structure and columns of both datasets.
- Prepared cleaned datasets for analysis.
- Organized match and delivery data for Power BI reporting.

### 2. SQL Analysis Using MySQL

Used SQL to explore IPL match and player performance.

SQL concepts applied during analysis include:

- SELECT, WHERE, ORDER BY
- GROUP BY and HAVING
- Aggregate Functions
- CASE Statements
- Joins
- Subqueries
- Common Table Expressions (CTEs)
- Window Functions

### 3. Power BI Dashboard Development

- Imported the cleaned datasets into Power BI.
- Created DAX measures for match, team, and player KPIs.
- Developed a four-page interactive dashboard.
- Designed charts to compare teams, players, seasons, and match strategies.
- Added interactive filters and navigation between dashboard pages.

## 📈 Power BI Dashboard

The dashboard consists of four pages, each focusing on a different area of IPL analytics.

### Page 1: Overview

\<details>
\<summary>View dashboard components\</summary>

**Key Performance Indicators:**

- Total Matches
- Total Runs
- Total Wickets
- Average First-Innings Score
- Highest Team Score
- Chase Win Percentage

**Visualizations:**

- Matches & Runs by Season
- Average Score by Season
- Match Result Distribution
- Matches by Venue
- Teams Wins by Winner

**Purpose:** Provides a high-level overview of IPL match statistics, season trends, venues, and team victories.

\</details>

### Page 2: Teams

\<details>
\<summary>View dashboard components\</summary>

**Key Performance Indicators:**

- Matches
- Wins
- Losses
- Win Percentage
- Average Score
- Highest Score

**Visualizations:**

- Win/Loss Trend
- Team Comparison (Win %)
- Average Score
- Toss Performance
- Toss Decision vs Match Result
- Team vs Team Comparison
- Season Performance

**Purpose:** Compares team performance, win percentages, toss outcomes, and performance trends across seasons.

\</details>

### Page 3: Players

\<details>
\<summary>View dashboard components\</summary>

**Key Performance Indicators:**

- Total Runs
- Total Wickets
- Average Strike Rate
- Average Economy
- Boundaries
- Dot Balls

**Visualizations:**

- Top Wicket Takers
- Batter Scatter
- Bowling Scatter
- Player statistics table
- Additional batting and bowling comparisons

**Purpose:** Evaluates individual player contributions and compares batting and bowling performance.

\</details>

### Page 4: Strategy

\<details>
\<summary>View dashboard components\</summary>

**Key Performance Indicators:**

- Toss Wins
- Toss to Match Conversion
- Chasing Wins %
- Batting First Win %
- Average First-Innings Score

**Visualizations:**

- Toss Decision vs Match Result
- Batting First vs Chasing
- Match strategy comparison table

**Purpose:** Examines toss decisions and match outcomes to understand the relationship between batting order and winning results.

\</details>

## 💡 Business & Analytical Questions

1. How many matches were played across the selected IPL seasons?
2. How did total runs and matches change season by season?
3. Which teams recorded the highest number of wins?
4. Which teams have the best win percentage?
5. How does team performance change across seasons?
6. Which teams perform better in head-to-head comparisons?
7. Which players are among the top wicket takers?
8. How can batting and bowling performances be compared?
9. How are toss decisions related to match results?
10. What is the difference between batting first and chasing?
11. What percentage of matches are won by teams chasing?
12. How does toss-to-match conversion vary?

## 📚 Key Learnings

Through this project, I gained practical experience in:

- Working with match-level and ball-by-ball cricket datasets.
- Using MySQL for data exploration and analysis.
- Writing SQL queries for team and player performance analysis.
- Creating DAX measures and KPI calculations.
- Building interactive Power BI dashboards.
- Comparing team and player performance.
- Analyzing toss decisions and match strategies.
- Presenting analytical findings through data visualizations.

