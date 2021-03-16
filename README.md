# Analysing ESG report using Natural Language Processing

## Summary
Environment, Social and Corporate Governance (ESG) refers to the three central factors in measuring the sustainability and societal impact of an investment in a company or business.  These criteria help to better determine the future financial performance of companies (return and risk).

This analysis extracts text from a ESG report in PDF format from the internet, performs NLP on these information, summaries the key ESG initiatives with Word Clouds, TDIDFs and discovers topics by building a Latent Dirichlet Allocation (LDA) model.

To keep this exercise as simple as possible, only one ESG report is being used.  Specifically the [Citibank's 2019 ESG report](https://www.citigroup.com/citi/about/esg/download/2019/Global-ESG-Report-2019.pdf?ieNocache=967).  

Given that ESG is a broad topic.  Different companies focus on different aspects of ESG depending on their business operations and culture.  One can potentially ingest more ESG reports from different companies across all sectors and industries to capture relevant ESG topics.  This to be attempted in another analysis.

## Notebook
1. https://github.com/edgetrader/esg-nlp/blob/master/notebook/esg-report-analysis.ipynb

## Reference

1. [A data-driven approach to Environmental, Social and Governance](https://databricks.com/blog/2020/07/10/a-data-driven-approach-to-environmental-social-and-governance.html)
2. [Higher ESG ratings are generally positively correlated with valuation and profitability while negatively correlated with volatility.](https://corpgov.law.harvard.edu/2020/01/14/esg-matters/)
3. [Topic Modeling with Gensim (Python)](https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/)
4. [Citibank's 2019 ESG report](https://www.citigroup.com/citi/about/esg/download/2019/Global-ESG-Report-2019.pdf?ieNocache=967)
5. [Databricks - ESG Reports](https://databricks.com/notebooks/esg_notebooks/01_esg_report.html)
5. [Databricks - Data Driven ESG Score](https://databricks.com/notebooks/esg_notebooks/02_esg_scoring.html)
6. [Databricks - ESG Market Risk](https://databricks.com/notebooks/esg_notebooks/03_esg_market.html)
7. [Topic Modeling and Latent Dirichlet Allocation (LDA) in Python](https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24)
8. [Evaluate Topic Models: Latent Dirichlet Allocation (LDA)](https://towardsdatascience.com/evaluate-topic-model-in-python-latent-dirichlet-allocation-lda-7d57484bb5d0)
9. [Topic modeling visualization – How to present the results of LDA models?](https://www.machinelearningplus.com/nlp/topic-modeling-visualization-how-to-present-results-lda-models/)

