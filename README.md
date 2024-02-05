# Private-Recommendation-Algorithm
- Abstract

 Due to the overwhelming number of options available on the internet, deciding where to have lunch in the office can be quite challenging. This paper presents a Personalized Restaurant Recommendation System designed to alleviate customer confusion. The system relies on customer preference features, which are collected through their reviews and personalized information.
 - Introduction
  This research tries to make personalized Recommendation system based on Collaborative Filtering Algorithms with the conditions which each user would sustain their preference so that it will influence on their future selection toward restaurants.
- Related Work


전영환 - 당신 취향의 맛집을 추천해드립니다: 장소 개인화 추천 시스템의 비밀(Naver Deview 2020)
History based POI (Point of Interest) Recommendation system.
Methodology: Collaborative Filtering
- Cons:
Lack of Personalization: Collaborative Filtering relies on the number of clicks customers have made, often leading to recommendations of generally popular restaurants that may not align with individual preferences.
- Low Accuracy:
Sparse Data: Restaurants are typically visited for specific purposes, unlike other categories such as music or shopping. Consequently, data collection frequency is low, resulting in a sparsity rate of 99.99%.
Matrix Folding: Matrix factorization can lead to issues due to incorrect handling of missing values within the algorithm. This can result in users and items with different preferences having highly similar dense vectors. This issue often arises because customer accessibility is confined to their place of residence. For example, people in Busan predominantly visit restaurants within Busan, implicitly partitioning unobserved data.
- Solutions to Address These Concerns:
POI-POI Interaction: If certain Points of Interest (POIs) co-occur with other specific POIs, they are considered similar. (Item embedding: Item co-occurrence Matrix Factorization)
Utilizing Pointwise Mutual Information: Implementing USER-POI interaction to manipulate expected Preference and Actual Preference, making them more similar.


- Knowledge Graph에게 맛집과 사용자를 묻는다: GNN으로 맛집 취향 저격하기- 전영환
This work serves as a supplement to the understanding of location, which was lacking in their work from the previous year. From the conclusion, we can extract valuable guidance for our future endeavors, which include:
1.	Defining the problem situation and context is crucial.
2.	Knowledge Graphs are powerful tools for representing specific domains.
3.	Tailoring Knowledge Graph design and modeling to the problem situation and context is essential.
4.	Understanding the characteristics of embeddings allows us to create suitable recommendation services and systems for each feature."
- Methodology
- To prevent a cold start, it is advisable to opt for content-based recommendation algorithms. Since our data is written in Korean, we need to transition from nltk to KoNLPy and KoBERT. In this work, it's important to differentiate words based on their part of speech, which is known as '유의미한 표현' (meaningful expression), such as verbs like '맛있어요' (delicious). Therefore, we will perform lemmatization on each word and segment Stop Words and non-Korean words.
- Experiments


