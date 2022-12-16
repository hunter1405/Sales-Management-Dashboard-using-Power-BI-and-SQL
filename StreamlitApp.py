import streamlit as st
from io import StringIO
import sys
from PIL import Image
import pandas as pd


st.set_page_config(page_title='Data Analyst Portfolio Project – Sales Management',page_icon="📶",layout="wide")

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://online.flippingbook.com/link/654193/" target="_blank">My Resume</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href=https://github.com/hunter1405?tab=repositories" target="_blank">Portfolio</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.facebook.com/hunter.dasick/" target="_blank">Facebook</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="www.linkedin.com/in/hung-tuan-nguyenf" target="_blank">Linkedin</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

h = st.markdown("""
<style>
div.fullScreenFrame > div {
    display: flex;
    justify-content: center;
}
</style>""", unsafe_allow_html=True)

#Title
original_title='<p style="text-align: center; color:#3498DB; text-shadow: 2px 2px 4px #000000; font-size: 60px;">Data Analyst Portfolio Project – Sales Management</p>'
st.markdown(original_title, unsafe_allow_html=True)


st.markdown("This is a project of **Nguyen Tuan Hung** from **UEL** that aims to create a Power BI dashboard overview of internet sales with graphs and KPIs comparing against budget. In addition, I created SQL query examples on data cleaning and data transformation for the project.")
st.markdown("You can find all the T-SQL statements below and the exported data that was created based on the SQL statements. This is the data I used to create dashboards and reports for the project.")        
st.markdown("https://github.com/tuanhung1405/Data-Analyst-Portfolio-Project-Sales-Management.git",unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
   st.write('')

with col2:
   st.header("Nguyen Tuan Hung")
   st.image("Nguyễn Tuấn Hưng_ Ảnh chân dung.png")

with col3:
   st.write('')



st.write('---')
    #st.sidebar.write("Choose your coin and the period")
    #coins = st.sidebar.selectbox("Which coin", (tup))
    #period = st.sidebar.selectbox("Choose the period", ("DAY", "1WEEK", "2WEEK", "MONTH"))
    
    # Store the initial value of widgets in session state
    

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
   st.image("Sales_Report (3)-1.png")
with col2:
   st.image("Sales_Report (3)-2.png")
with col3:
   st.image("pic1.png")
with col4:
   st.image("pic2.png")
with col5:
   st.image("pic3.png")


         
        
st.header('Business Request & User Stories')
st.write("The business request for this data analyst project was an executive sales report for sales managers. Based on the request that was made from the business we following user stories were defined to fulfill delivery and ensure that acceptance criteria’s were maintained throughout the project.")
data = {"As a (role)": ['Sales Manager', 'Sales Representative', 'Sales Representative', 'Sales Manager'],
         "I want (request / demand)": ['To get a dashboard overview of internet sales', 'A detailed overview of Internet Sales per Customer', 'A detailed overview of Internet Sales per Products', 'A dashboard overview of internet salesr'],
         "So that I (user value)": ['Can follow better which customers and products sells the best', 'Can follow up my customers that buys the most and who we can sell more to', 'Can follow up my Products that sells the most', 'Follow sales over time against budgetr'],
         "Acceptance Criteria": ['A Power BI dashboard which updates data once a day', 'A Power BI dashboard which allows me to filter data for each customer', 'A Power BI dashboard which allows me to filter data for each Product', 'A Power Bi dashboard with graphs and KPIs comparing against budget.']}

df = pd.DataFrame(data)
st.table(df)
st.write('---')

st.header('Data Cleansing & Transformation (SQL)')
st.write("""To create the necessary data model for doing analysis and fulfilling the business needs defined in the user stories the following tables were extracted using SQL.

One data source (sales budgets) were provided in Excel format and were connected in the data model in a later step of the process.

Below are the SQL statements for cleansing and transforming necessary data.
""")

st.subheader('DIM_Calendar:')
code = '''-- Cleansed DIM_Date Table --
SELECT 
  [DateKey], 
  [FullDateAlternateKey] AS Date, 
  --[DayNumberOfWeek], 
  [EnglishDayNameOfWeek] AS Day, 
  --[SpanishDayNameOfWeek], 
  --[FrenchDayNameOfWeek], 
  --[DayNumberOfMonth], 
  --[DayNumberOfYear], 
  --[WeekNumberOfYear],
  [EnglishMonthName] AS Month, 
  Left([EnglishMonthName], 3) AS MonthShort,   -- Useful for front end date navigation and front end graphs.
  --[SpanishMonthName], 
  --[FrenchMonthName], 
  [MonthNumberOfYear] AS MonthNo, 
  [CalendarQuarter] AS Quarter, 
  [CalendarYear] AS Year --[CalendarSemester], 
  --[FiscalQuarter], 
  --[FiscalYear], 
  --[FiscalSemester] 
FROM 
 [AdventureWorksDW2019].[dbo].[DimDate]
WHERE 
  CalendarYear >= 2019'''
st.code(code, language='sql')

st.subheader('DIM_Customers:')
code = '''-- Cleansed DIM_Customers Table --
SELECT 
  c.customerkey AS CustomerKey, 
  --      ,[GeographyKey]
  --      ,[CustomerAlternateKey]
  --      ,[Title]
  c.firstname AS [First Name], 
  --      ,[MiddleName]
  c.lastname AS [Last Name], 
  c.firstname + ' ' + lastname AS [Full Name], 
  -- Combined First and Last Name
  --      ,[NameStyle]
  --      ,[BirthDate]
  --      ,[MaritalStatus]
  --      ,[Suffix]
  CASE c.gender WHEN 'M' THEN 'Male' WHEN 'F' THEN 'Female' END AS Gender,
  --      ,[EmailAddress]
  --      ,[YearlyIncome]
  --      ,[TotalChildren]
  --      ,[NumberChildrenAtHome]
  --      ,[EnglishEducation]
  --      ,[SpanishEducation]
  --      ,[FrenchEducation]
  --      ,[EnglishOccupation]
  --      ,[SpanishOccupation]
  --      ,[FrenchOccupation]
  --      ,[HouseOwnerFlag]
  --      ,[NumberCarsOwned]
  --      ,[AddressLine1]
  --      ,[AddressLine2]
  --      ,[Phone]
  c.datefirstpurchase AS DateFirstPurchase, 
  --      ,[CommuteDistance]
  g.city AS [Customer City] -- Joined in Customer City from Geography Table
FROM 
  [AdventureWorksDW2019].[dbo].[DimCustomer] as c
  LEFT JOIN dbo.dimgeography AS g ON g.geographykey = c.geographykey 
ORDER BY 
  CustomerKey ASC -- Ordered List by CustomerKey'''
st.code(code, language='sql')

st.subheader('DIM_Products:')
code = '''-- Cleansed DIM_Products Table --
SELECT 
  p.[ProductKey], 
  p.[ProductAlternateKey] AS ProductItemCode, 
  --      ,[ProductSubcategoryKey], 
  --      ,[WeightUnitMeasureCode]
  --      ,[SizeUnitMeasureCode] 
  p.[EnglishProductName] AS [Product Name], 
  ps.EnglishProductSubcategoryName AS [Sub Category], -- Joined in from Sub Category Table
  pc.EnglishProductCategoryName AS [Product Category], -- Joined in from Category Table
  --      ,[SpanishProductName]
  --      ,[FrenchProductName]
  --      ,[StandardCost]
  --      ,[FinishedGoodsFlag] 
  p.[Color] AS [Product Color], 
  --      ,[SafetyStockLevel]
  --      ,[ReorderPoint]
  --      ,[ListPrice] 
  p.[Size] AS [Product Size], 
  --      ,[SizeRange]
  --      ,[Weight]
  --      ,[DaysToManufacture]
  p.[ProductLine] AS [Product Line], 
  --     ,[DealerPrice]
  --      ,[Class]
  --      ,[Style] 
  p.[ModelName] AS [Product Model Name], 
  --      ,[LargePhoto]
  p.[EnglishDescription] AS [Product Description], 
  --      ,[FrenchDescription]
  --      ,[ChineseDescription]
  --      ,[ArabicDescription]
  --      ,[HebrewDescription]
  --      ,[ThaiDescription]
  --      ,[GermanDescription]
  --      ,[JapaneseDescription]
  --      ,[TurkishDescription]
  --      ,[StartDate], 
  --      ,[EndDate], 
  ISNULL (p.Status, 'Outdated') AS [Product Status] 
FROM 
  [AdventureWorksDW2019].[dbo].[DimProduct] as p
  LEFT JOIN dbo.DimProductSubcategory AS ps ON ps.ProductSubcategoryKey = p.ProductSubcategoryKey 
  LEFT JOIN dbo.DimProductCategory AS pc ON ps.ProductCategoryKey = pc.ProductCategoryKey 
order by 
  p.ProductKey asc'''
st.code(code, language='sql')

st.subheader('FACT_InternetSales:')
code = '''-- Cleansed FACT_InternetSales Table --
SELECT 
  [ProductKey], 
  [OrderDateKey], 
  [DueDateKey], 
  [ShipDateKey], 
  [CustomerKey], 
  --  ,[PromotionKey]
  --  ,[CurrencyKey]
  --  ,[SalesTerritoryKey]
  [SalesOrderNumber], 
  --  [SalesOrderLineNumber], 
  --  ,[RevisionNumber]
  --  ,[OrderQuantity], 
  --  ,[UnitPrice], 
  --  ,[ExtendedAmount]
  --  ,[UnitPriceDiscountPct]
  --  ,[DiscountAmount] 
  --  ,[ProductStandardCost]
  --  ,[TotalProductCost] 
  [SalesAmount] --  ,[TaxAmt]
  --  ,[Freight]
  --  ,[CarrierTrackingNumber] 
  --  ,[CustomerPONumber] 
  --  ,[OrderDate] 
  --  ,[DueDate] 
  --  ,[ShipDate] 
FROM 
  [AdventureWorksDW2019].[dbo].[FactInternetSales]
WHERE 
  LEFT (OrderDateKey, 4) >= YEAR(GETDATE()) -2 -- Ensures we always only bring two years of date from extraction.
ORDER BY
  OrderDateKey ASC'''
st.code(code, language='sql')
st.write('---')


st.header('Data Model')
st.write("""Below is a screenshot of the data model after cleansed and prepared tables were read into Power BI.

This data model also shows how FACT_Budget hsa been connected to FACT_InternetSales and other necessary DIM tables.""")
st.image("datamodel-1.png")
st.write('---')


st.header('Sales Management Dashboard')
st.write("""The finished sales management dashboard with one page with works as a dashboard and overview, with two other pages focused on combining tables for necessary details and visualizations to show sales over time, per customers and per products.""")
st.write("**Click the link to to open the dashboard and try it out!**")


import streamlit.components.v1 as components

st.markdown("https://app.powerbi.com/links/my5rQKhiQL?ctid=07acb355-56bc-489b-b98c-8fea440460e8&pbi_source=linkShare&bookmarkGuid=3ab7991c-d111-4774-bcbf-e2a4380e2d4f",unsafe_allow_html=True)

col1, col2= st.columns(2)
with col1:
  st.image("Sales_Report (3)-1.png")
with col2:
  st.image("Sales_Report (3)-2.png")
