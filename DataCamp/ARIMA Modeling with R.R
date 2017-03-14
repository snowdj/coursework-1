## 1 - Time Series Data and Models

##--
## Data Play

## In the video, you saw various types of data. In this exercise, you will plot additional time series data and compare them to what you saw in the video. It is useful to think about how these time series compare to the series in the video. In particular, concentrate on the type of trend, seasonality or periodicity, and homoscedasticity.

## Before you use a data set for the first time, you should use the help system to see the details of the data. For example, use help(AirPassengers) or ?AirPassengers to see the details of the series.
## Instructions

##     The packages astsa and xts are preloaded in your R environment.
##     Use help() to view the specifics of the AirPassengers data file.
##     Use plot() to plot the airline passenger data (AirPassengers) and compare it to a series you saw in the video.
##     Plot the DJIA daily closings (djia$Close) and compare it to a series you saw in the video.
##     Plot the Southern Oscillation Index (soi) and inspect it for trend, seasonality, and homoscedasticity.

# View a detailed description of AirPassengers
help(AirPassengers)

# Plot AirPassengers
plot(AirPassengers)

# Plot the DJIA daily closings
plot(djia$Close)

# Plot the Southern Oscillation Index
plot(soi)


##--
Elements of Time Series

Look at the AirPassengers series again. Select the answer that is FALSE.
Possible Answers
    There is seasonality.
    There is trend.
    There is heteroscedasticity.
  * The series is white noise.
    Over the time period of this data, it was still ok to smoke on planes.


##--
## Differencing

## As seen in the video, when a time series is trend stationary, it will have stationary behavior around a trend. A simple example is Yt=α+βt+Xt where Xt is stationary.

## A different type of model for trend is random walk, which has the form Xt=Xt−1+Wt
## , where Wt is white noise. It is called a random walk because at time t the process is where it was at time t−1

## plus a completely random movement. For a random walk with drift, a constant is added to the model and will cause the random walk to drift in the direction (positve or negative) of the drift.

## We simulated and plotted data from these models. Note the difference in the behavior of the two models.

## In both cases, simple differencing can remove the trend and coerce the data to stationarity. Differencing looks at the difference between the value of a time series at a certain point in time and its preceding value. That is, Xt−Xt−1

## is computed.

## To check that it works, you will difference each generated time series and plot the detrended series. If a time series is in x, then diff(x) will have the detrended series obtained by differencing the data. To plot the detrended series, simply use plot(diff(x)).
## Instructions

##     In one line, difference and plot the detrended trend stationary data in y by nesting a call to diff() within a call to plot(). Does the result look stationary?
##     Do the same for x. Does the result look stationary?

# Plot detrended y (trend stationary)
plot(diff(y))

# Plot detrended x (random walk)
plot(diff(x))


##--
## Detrending Data

## As you have seen in the previous exercise, differencing is generally good for removing trend from time series data. Recall that differencing looks at the difference between the value of a time series at a certain point in time and its preceding value.

## In this exercise, you will use differencing diff() to detrend and plot real time series data.
## Instructions

##     The package astsa is preloaded.
##     Generate a multifigure plot comparing the global temperature data (globtemp) with the detrended series. You can create a multifigure plot by running the pre-written par() command followed by two separate calls to plot().
##     Generate another multifigure plot comparing the weekly cardiovascular mortality in Los Angeles County (cmort) with the detrended series.

# Plot globtemp and detrended globtemp
par(mfrow = c(2,1))
plot(globtemp) 
plot(diff(globtemp))

# Plot cmort and detrended cmort
par(mfrow = c(2,1))
plot(cmort)
plot(diff(cmort))


##--
## Dealing with Trend and Heteroscedasticity

## Here, we will coerce nonstationary data to stationarity by calculating the return or growth rate as follows.

## Often time series are generated as
## Xt=(1+pt)Xt−1
## meaning that the value of the time series observed at time t equals the value observed at time t−1 and a small percent change pt at time t.

## A simple deterministic example is putting money into a bank with a fixed interest p. In this case, Xt is the value of the account at time period t with an initial deposit of X0.

## Typically, pt is referred to as the return or growth rate of a time series, and this process is often stable.

## For reasons that are outside the scope of this course, it can be shown that the growth rate pt can be approximated by
## Yt=logXt−logXt−1≈pt.

## In R, pt is often calculated as diff(log(x)) and plotting it can be done in one line plot(diff(log(x))).
## Instructions
##     As before, the packages astsa and xts are preloaded.
##     Generate a multifigure plot to (1) plot the quarterly US GNP (gnp) data and notice it is not stationary, and (2) plot the approximate growth rate of the US GNP using diff() and log().
##     Use a multifigure plot to (1) plot the daily DJIA closings (djia$Close) and notice that it is not stationary. The data are an xts object. Then (2) plot the approximate DJIA returns using diff() and log(). How does this compare to the growth rate of the GNP?

# astsa and xts are preloaded 

# Plot GNP series (gnp) and its growth rate
par(mfrow = c(2,1))
plot(gnp)
plot(diff(log(gnp)))

# Plot DJIA closings (djia$Close) and its returns
par(mfrow = c(2,1))
plot(djia$Close)
plot(diff(log(djia$Close)))


##--
## Simulating ARMA Models

## As we saw in the video, any stationary time series can be written as a linear combination of white noise. In addition, any ARMA model has this form, so it is a good choice for modeling stationary time series.

## R provides a simple function called arima.sim() to generate data from an ARMA model. For example, the syntax for generating 100 observations from an MA(1) with parameter .9 is arima.sim(model = list(order = c(0, 0, 1), ma = .9 ), n = 100). You can also use order = c(0, 0, 0) to generate white noise.

## In this exercise, you will generate data from various ARMA models. For each command, generate 200 observations and plot the result.
## Instructions
##     Use arima.sim() and plot() to generate and plot white noise.
##     Use arima.sim() and plot() to generate and plot an MA(1) with parameter .9.
##     Use arima.sim() and plot() to generate and plot an AR(2) with parameters 1.5 and -.75.

# Generate and plot white noise
WN <- arima.sim(model = list(order = c(0, 0, 0)), n = 200)
plot(WN)

# Generate and plot an MA(1) with parameter .9 
MA <- arima.sim(model = list(order = c(0, 0, 1), ma = .9), n = 200)
plot(MA)

# Generate and plot an AR(2) with parameters 1.5 and -.75
AR <- arima.sim(model = list(order = c(2, 0, 0), ar = c(1.5, -.75)), n = 200)
plot(AR)




## 2 - Fitting ARMA models

##--
## Fitting an AR(1) Model

## Recall that you use the ACF and PACF pair to help identify the orders p
## and q of an ARMA model. The following table is a summary of the results:
## 	AR(p)             	MA(q) 	                ARMA(p,q)
## ACF 	Tails off 	        Cuts off after lag q	Tails off
## PACF 	Cuts off after lag p	Tails off 	        Tails off

## In this exercise, you will generate data from the AR(1) model,
## Xt=.9Xt−1+Wt,

## look at the simulated data and the sample ACF and PACF pair to determine the order. Then, you will fit the model and compare the estimated parameters to the true parameters.

## Throughout this course, you will be using sarima() from the astsa package to easily fit models to data. The command produces a residual diagnostic graphic that can be ignored until diagnostics is discussed later in the chapter.
## Instructions
##     The package astsa is preloaded.
##     Use the prewritten arima.sim() command to generate 100 observations from an AR(1) model with AR parameter .9. Save this to x.
##     Plot the generated data using plot().
##     Plot the sample ACF and PACF pairs using the acf2() command from the astsa package.
##     Use sarima() from astsa to fit an AR(1) to the previously generated data. Examine the t-table and compare the estimates to the true values. For example, if the time series is in x, to fit an AR(1) to the data, use sarima(x, p = 1, d = 0, q = 0) or simply sarima(x, 1, 0, 0).

# Generate 100 observations from the AR(1) model
x <- arima.sim(model = list(order = c(1, 0, 0), ar = .9), n = 100) 

# Plot the generated data 
plot(x)

# Plot the sample P/ACF pair
acf2(x)

# Fit an AR(1) to the data and examine the t-table
sarima(x, p = 1, d = 0, q = 0)


##--
## Fitting an AR(2) Model

## For this exercise, we generated data from the AR(2) model,
## Xt=1.5Xt−1−.75Xt−2+Wt,

## using x <- arima.sim(model = list(order = c(2, 0, 0), ar = c(1.5, -.75)), n = 200). Look at the simulated data and the sample ACF and PACF pair to determine the model order. Then fit the model and compare the estimated parameters to the true parameters.
## Instructions

##     The package astsa is preloaded. x contains the 200 AR(2) observations.
##     Use plot() to plot the generated data in x.
##     Plot the sample ACF and PACF pair using acf2() from the astsa package.
##     Use sarima() to fit an AR(2) to the previously generated data in x. Examine the t-table and compare the estimates to the true values.

# astsa is preloaded

# Plot x
plot(x)

# Plot the sample P/ACF of x
acf2(x)

# Fit an AR(2) to the data and examine the t-table
sarima(x, p = 2, d = 0, q = 0)


##--
## Fitting an MA(1) Model

## In this exercise, we generated data from an MA(1) model,
## Xt=Wt−.8Wt−1,

## x <- arima.sim(model = list(order = c(0, 0, 1), ma = -.8), n = 100). Look at the simulated data and the sample ACF and PACF to determine the order based on the table given in the first exercise. Then fit the model.

## Recall that for pure MA(q) models, the theoretical ACF will cut off at lag q while the PACF will tail off.
## Instructions

##     The package astsa is preloaded. 100 MA(1) observations are available in your workspace as x.
##     Use plot() to plot the generated data in x.
##     Plot the sample ACF and PACF pairs using acf2() from the astsa package.
##     Use sarima() from astsa to fit an MA(1) to the previously generated data. Examine the t-table and compare the estimates to the true values.

# astsa is preloaded

# Plot x
plot(x)

# Plot the sample P/ACF of x
acf2(x)

# Fit an MA(1) to the data and examine the t-table
sarima(x, p = 0, d = 0, q = 1)


##--
## Fitting an ARMA model

## You are now ready to merge the AR model and the MA model into the ARMA model. We generated data from the ARMA(2,1) model,
## Xt=Xt−1−.9Xt−2+Wt+.8Wt−1,

## x <- arima.sim(model = list(order = c(2, 0, 1), ar = c(1, -.9), ma = .8), n = 250). Look at the simulated data and the sample ACF and PACF pair to determine a possible model.

## Recall that for ARMA(p,q) models, both the theoretical ACF and PACF tail off. In this case, the orders are difficult to discern from data and it may not be clear if either the sample ACF or sample PACF is cutting off or tailing off. In this case, you know the actual model orders, so fit an ARMA(2,1) to the generated data. General modeling strategies will be discussed further in the course.
## Instructions
##     The package astsa is preloaded. 250 ARMA(2,1) observations are in x.
##     As in the previous exercises, use plot() to plot the generated data in x and use acf2() to view the sample ACF and PACF pairs.
##     Use sarima() to fit an ARMA(2,1) to the generated data. Examine the t-table and compare the estimates to the true values.

# astsa is preloaded

# Plot x
plot(x)

# Plot the sample P/ACF of x
acf2(x)

# Fit an ARMA(2,1) to the data and examine the t-table
sarima(x, p = 2, d = 0, q = 1)


##--
## Model Choice - I
## Based on the sample P/ACF pair of the logged and differenced varve data (dl_varve), an MA(1) was indicated. The best approach to fitting ARMA is to start with a low order model, and then try to add a parameter at a time to see if the results change.

## In this exercise, you will fit various models to the dl_varve data and note the AIC and BIC for each model. In the next exercise, you will use these AICs and BICs to choose a model. Remember that you want to retain the model with the smallest AIC and/or BIC value.

## A note before you start:
## sarima(x, p = 0, d = 0, q = 1) and sarima(x, 0, 0, 1)
## are the same.
## Instructions
##     The package astsa is preloaded. The varve series has been logged and differenced as dl_varve <- diff(log(varve)).
##     Use sarima() to fit an MA(1) to dl_varve. Take a close look at the output of your sarima() command to see the AIC and BIC for this model.
##     Repeat the previous exercise, but add an MA parameter by fitting an MA(2) model. Based on AIC and BIC, is this an improvement over the previous model?
##     Instead of adding an MA parameter, add an AR parameter to the original MA(1) fit. That is, fit an ARMA(1,1) to dl_varve. Based on AIC and BIC, is this an improvement over the previous models?

# Fit an MA(1) to dl_varve.   
sarima(dl_varve, p=0, d=0, q=1)

# Fit an MA(2) to dl_varve. Improvement?
sarima(dl_varve, p=0, d=0, q=1)

# Fit an ARMA(1,1) to dl_varve. Improvement?
sarima(varve, p=1, d=0, q=1)

## AIC and BIC help you find the model with the smallest error using the least number of parameters. The idea is based on the parsimony principle, which is basic to all science and tells you to choose the simplest scientific explanation that fits the evidence.


##--
## Model Choice - II

## In the previous exercise, you fit three different models to the logged and differenced varve series (dl_varve). The data are displayed to the right. The extracted AIC and BIC from each run are tabled below.
## Model 	AIC 	BIC
## MA(1) 	-0.4437 	-1.4366
## MA(2) 	-0.4659 	-1.4518
## ARMA(1,1) 	-0.4702 	-1.4561


## Using the table, indicate which statement below is FALSE.
## Possible Answers
##     AIC and BIC both prefer the ARMA(1,1) model over the other fitted models.
##   * AIC prefers the MA(1) model.
##     BIC prefers the MA(2) over the MA(1)
##     Because they use different penalties, the AIC and BIC can prefer different models.

## Exactly! The lowest AIC value of the three models is the ARMA(1,1) model, meaning AIC prefers that model over the MA(1) model.


##--
## Residual Analysis - I

## As you saw in the video, an sarima() run includes a residual analysis graphic. Specifically, the output shows (1) the standardized residuals, (2) the sample ACF of the residuals, (3) a normal Q-Q plot, and (4) the p-values corresponding to the Box-Ljung-Pierce Q-statistic.

## In each run, check the four residual plots as follows:

##    1. The standardized residuals should behave as a white noise sequence with mean zero and variance one. Examime the residual plot for departures from this behavior.
##    2. The sample ACF of the residuals should look like that of white noise. Examine the ACF for departures from this behavior.
##    3. Normality is an essential assumption when fitting ARMA models. Examine the Q-Q plot for departures from normality and to identify outliers.
##    4. Use the Q-statistic plot to help test for departures from whiteness of the residuals.

## As in the previous exercise, dl_varve <- diff(log(varve)), which is plotted below a plot of varve. The astsa package is preloaded.

## Instructions
##     Use sarima() to fit an MA(1) to dl_varve and do a complete residual analysis as prescribed above. Make a note of what you see for the next exercise.
##     Use another call to sarima() to fit an ARMA(1,1) to dl_varve and do a complete residual analysis as prescribed above. Again, make a note of what you see for the next exercise.

# Fit an MA(1) to dl_varve. Examine the residuals  
sarima(dl_varve, p = 0, d = 0, q = 1)

# Fit an ARMA(1,1) to dl_varve. Examine the residuals
sarima(dl_varve, p = 1, d = 0, q = 1)


##--
## Residual Analysis - II

## In the previous exercise, you fit two different ARMA models to the logged and differenced varve series: an MA(1) and an ARMA(1,1) model. The residual analysis graphics are displayed in order of the run:
##     MA(1)
##     ARMA(1, 1)

## Which of the following statements is FALSE (partially truthful statements are false - data analysis is not politics)?
## Possible Answers
##     The residuals for the MA(1) model are not white noise.
##     The residuals for the ARMA(1, 1) model appear to be Gaussian white noise.
##   * It is not a good idea to look at the residual analysis because it might tell you if your model is incorrect and you might have to stay late at work to figure out the correct model. 

## You should always examine the residuals because the model assumes the errors are Gaussian white noise.


##--
## ARMA get in

## By now you have gained considerable experience fitting ARMA models to data, but before you start celebrating, try one more exercise (sort of) on your own.

## The data in oil are crude oil, WTI spot price FOB (in dollars per barrel), weekly data from 2000 to 2008. Use your skills to fit an ARMA model to the returns. The weekly crude oil prices (oil) are plotted for you. Throughout the exercise, work with the returns, which you will calculate.

## As before, the astsa package is preloaded for you. The data are preloaded as oil and plotted on the right.

## Instructions
##     Calculate the approximate crude oil price returns using diff() and log(). Put the returns in oil_returns.
##     Plot oil_returns and notice that there are a couple of outliers prior to 2004. Convince yourself that the returns are stationary.
##     Plot the sample ACF and PACF of the oil_returns using acf2() from the astsa package.
##     From the P/ACF pair, it is apparent that the correlations are small and the returns are nearly noise. But it could be that both the ACF and PACF are tailing off. If this is the case, then an ARMA(1,1) is suggested. Fit this model to the oil returns using sarima(). Does the model fit well? Can you see the outliers in the residual plot?

# Calculate approximate oil returns
oil_returns <- diff(log(oil))

# Plot oil_returns. Notice the outliers.
plot(oil_returns)

# Plot the P/ACF pair for oil_returns
acf2(oil_returns)

# Assuming both P/ACF are tailing, fit a model to oil_returns
sarima(oil_returns, p = 1, d = 0, q = 1)




## 3 - ARIMA Models

##--
## ARIMA - Plug and Play

## As you saw in the video, a time series is called ARIMA(p,d,q) if the differenced series (of order d) is ARMA(p,q).

## To get a sense of how the model works, you will analyze simulated data from the integrated model
## Yt=.9Yt−1+Wt
## where Yt=∇Xt=Xt−Xt−1. In this case, the model is an ARIMA(1,1,0) because the differenced data are an autoregression of order one.

## The simulated time series is in x and it was generated in R as
## x <- arima.sim(model = list(order = c(1, 1, 0), ar = .9), n = 200).

## You will plot the generated data and the sample ACF and PACF of the generated data to see how integrated data behave. Then, you will difference the data to make it stationary. You will plot the differenced data and the corresponding sample ACF and PACF to see how differencing makes a difference.

## As before, the astsa package is preloaded in your workspace. Data from an ARIMA(1,1,0) with AR parameter .9 is saved in object x.
## Instructions
##     Plot the generated data.
##     Use acf2() from astsa to plot the sample P/ACF pair for the generated data.
##     Plot the differenced data.
##     Use another call to acf2() to view the sample P/ACF pair for the differenced data. Note how they imply an AR(1) model for the differenced data.

# Plot x
plot(x)

# Plot the P/ACF pair of x
acf2(x)

# Plot the differenced data
plot(diff(x))

# Plot the P/ACF pair of the differenced data
acf2(diff(x))


##--
## Simulated ARIMA

## Before analyzing actual time series data, you should try working with a slightly more complicated model.

## Here, we generated 250 observations from the ARIMA(2,1,0) model with drift given by
## Yt=1+1.5Yt−1−.75Yt−2+Wt
## where Yt=∇Xt=Xt−Xt−1.

## You will use the established techniques to fit a model to the data.

## The astsa package is preloaded and the generated data are in x. The series x and the detrended series y <- diff(x) have been plotted.
## Instructions
##     Plot the sample ACF and PACF using acf2() of the differenced data diff(x) to determine a model.
##     Fit an ARIMA(2,1,0) model using sarima() to the generated data. Examine the t-table and other output information to assess the model fit.

# Plot sample P/ACF of differenced data and determine model
acf2(diff(x))

# Estimate parameters and examine output
sarima(x, p = 2, d = 1, q = 0)


##--
## Global Warming

## Now that you have some experience fitting an ARIMA model to simulated data, your next task is to apply your skills to some real world data.

## The data in globtemp (from astsa) are the annual global temperature deviations to 2015. In this exercise, you will use established techniques to fit an ARIMA model to the data. A plot of the data shows random walk behavior, which suggests you should work with the differenced data. The differenced data diff(globtemp) are also plotted.

## After plotting the sample ACF and PACF of the differenced data diff(globtemp), you can say that either
##     The ACF and the PACF are both tailing off, implying an ARIMA(1,1,1) model.
##     The ACF cuts off at lag 2, and the PACF is tailing off, implying an ARIMA(0,1,2) model.
##     The ACF is tailing off and the PACF cuts off at lag 3, implying an ARIMA(3,1,0) model. Although this model fits reasonably well, it is the worst of the three (you can check it) because it uses too many parameters for such small autocorrelations.

## After fitting the first two models, check the AIC and BIC to choose the preferred model.
## Instructions
##     Plot the sample ACF and PACF of the differenced data, diff(globtemp), to discover that 2 models seem reasonable, an ARIMA(1,1,1) and an ARIMA(0,1,2).
##     Use sarima() to fit an ARIMA(1,1,1) model to globtemp. Are all the parameters significant?
##     Use another call to sarima() to fit an ARIMA(0,1,2) model to globtemp. Are all the parameters significant? Which model is better?

# Plot the sample P/ACF pair of the differenced data 
acf2(diff(globtemp))

# Fit an ARIMA(1,1,1) model to globtemp
sarima(globtemp, p = 1, d = 1, q = 1)

# Fit an ARIMA(0,1,2) model to globtemp. Which model is better?
sarima(globtemp, p = 0, d = 1, q = 2)

## As you can see from the t-table, the second MA parameter is not significantly different from zero and the first MA parameter is approximately the same in each run. Also, the AIC and BIC both increase when the parameter is added. In addition, the residual analysis of your ARIMA(0,1,1) model is fine. All of these facts together indicate that you have a successful model fit. 


##--
## Diagnostics - Global Temperatures

## You can now finish your analysis of global temperatures. Recall that you previously fit two models to the data in globtemp, an ARIMA(1,1,1) and an ARIMA(0,1,2). In the final analysis, check the residual diagnostics and use AIC and BIC for model choice.

## The data are plotted for you.
## Instructions
##     Fit an ARIMA(0,1,2) model to globtemp and check the diagnositcs. What does the output tell you about the model?
##     Fit an ARIMA(1,1,1) model to globtemp and check the diagnostics.
##     Which is the better model? Type your answer into the blanks in your R workspace (ex. either ARIMA(0,1,2) or ARIMA(1,1,1)).

# Fit ARIMA(0,1,2) to globtemp and check diagnostics  
sarima(globtemp, p = 0, d = 1, q = 2) 

# Fit ARIMA(1,1,1) to globtemp and check diagnostics
sarima(globtemp, p = 1, d = 1, q = 1)

# Which is the better model?
"ARIMA(0,1,2)"

## Your model diagnostics suggest that both the ARIMA(0,1,2) and the ARIMA(1,1,1) are reasonable models. However, the AIC and BIC suggest that the ARIMA(0,1,2) performs slightly better, so this should be your preferred model. Although you were not asked to do so, you can use overfitting to assess the final model. For example, try fitting an ARIMA(1,1,2) or an ARIMA(0,1,3) to the data.


##--
## Forecasting Simulated ARIMA

## Now that you are an expert at fitting ARIMA models, you can use your skills for forecasting. First, you will work with simulated data.

## We generated 120 observations from an ARIMA(1,1,0) model with AR parameter .9. The data are in y and the first 100 observations are in x. These observations are plotted for you. You will fit an ARIMA(1,1,0) model to the data in x and verify that the model fits well. Then use sarima.for() from astsa to forecast the data 20 time periods ahead. You will then compare the forecasts to the actual data in y.

## The basic syntax for forecasting is sarima.for(data, n.ahead, p, d, q) where n.ahead is a positive integer that specifies the forecast horizon. The predicted values and their standard errors are printed, the data are plotted in black, and the forecasts are in red along with 2 mean square prediction error bounds as blue dashed lines.

## The astsa package is preloaded and the data (x) and differenced data (diff(x)) are plotted.
## Instructions

##     Plot the sample ACF and PACF of the differenced data to determine a model.
##     Use sarima() to fit an ARIMA(1,1,0) to the data. Examine the output of your sarima() command to assess the fit and model diagnostics.
##     Use sarima.for() to forecast the data 20 time periods ahead. Compare it to the actual values.

# Plot P/ACF pair of differenced data 
acf2(diff(x))

# Fit model - check t-table and diagnostics
sarima(x, p = 1, d = 1, q = 0)

# Forecast the data 20 time periods ahead
sarima.for(x, n.ahead = 20, p = 1, d = 1, q = 0) 
lines(y)  


##--
## Forecasting Global Temperatures

## Now you can try forecasting real data.

## Here, you will forecast the annual global temperature deviations globtemp to 2050. Recall that in previous exercises, you fit an ARIMA(0,1,2) model to the data. You will refit the model to confirm it, and then forecast the series 35 years into the future.

## The astsa package is preloaded and the data are plotted.
## Instructions

##     Fit an ARIMA(0,1,2) model to the data using sarima(). Based on your previous analysis this was the best model for the globtemp data. Recheck the parameter significance in the t-table output and check the residuals for any departures from the model assumptions.
##     Use sarima.for() to forceast your global temperature data 35 years ahead to 2050 using the ARIMA(0,1,2) fit.

# Fit an ARIMA(0,1,2) to globtemp and check the fit
sarima(globtemp, p = 0, d = 1, q = 2)

# Forecast data 35 years into the future
sarima.for(globtemp, n.ahead = 35, p = 0, d = 1, q = 2)




## 4 - Seasonal ARIMA

##--
## P/ACF of Pure Seasonal Models

## In the video, you saw that a pure seasonal ARMA time series is correlated at the seasonal lags only. Consequently, the ACF and PACF behave as the nonseasonal counterparts, but at the seasonal lags, 1S, 2S, ..., where S is the seasonal period (S = 12 for monthly data). As in the nonseasonal case, you have the pure seasonal table:

## Behavior of the ACF and PACF for Pure SARMA Models
## 	AR(P)S 	MA(Q)S 	ARMA(P,Q)S
## ACF* 	Tails off at
## seasonal lags 	Cuts off
## after lag QS 	Tails off at
## seasonal lags
## PACF* 	Cuts off
## after lag PS 	Tails off at
## seasonal lags 	Tails off at
## seasonal lags

## *The values at nonseasonal lags are zero.

## We have plotted the true ACF and PACF of a pure seasonal model. Identify the model with the following abbreviations SAR(P)S, SMA(Q)S, or SARMA(P,Q)S for the pure seasonal AR, MA or ARMA with seasonal period S, respectively.
## Possible Answers
##     SARMA(1,1)12
##   * SAR(1)12
##     SMA(1)12
##     SMA(96)12 

## The ACF tails off at seasonal lags, while the PACF cuts off after lag 12. This fits with a SAR(1)12 model.


##--
## Fit a Pure Seasonal Model

## As with other models, you can fit seasonal models in R using the sarima() command in the astsa package.

## To get a feeling of how pure seasonal models work, it is best to consider simulated data. We generated 250 observations from a pure seasonal model given by
## Xt=.9Xt−12+Wt+.5Wt−12,

## which we would denote as a SARMA(P = 1, Q = 1)S = 12. Three years of data and the model ACF and PACF are plotted for you.

## You will compare the sample ACF and PACF values from the generated data to the true values displayed to the right.

## The astsa package is preloaded for you and the generated data are in x.
## Instructions
##     Use acf2() to plot the sample ACF and PACF of the generated data to lag 60 and compare to actual values. To estimate to lag 60, set the max.lag argument equal to 60.
##     Fit the model to generated data using sarima(). In addition to the p, d, and q arguments in your sarima() command, specify P, D, Q, and S (note that R is case sensitive).

# Plot sample P/ACF to lag 60 and compare to the true values
acf2(x, max.lag = 60)

# Fit the seasonal model to x
sarima(x, p = 0, d = 0, q = 0, P = 1, D = 0, Q = 1, S = 12)


##--
## Fit a Mixed Seasonal Model

## Pure seasonal dependence such as that explored earlier in this chapter is relatively rare. Most seasonal time series have mixed dependence, meaning only some of the variation is explained by seasonal trends.

## Recall that the full seasonal model is denoted by SARIMA(p,d,q)x(P,D,Q)S where capital letters denote the seasonal orders.

## As before, this exercise asks you to compare the sample P/ACF pair to the true values for some simulated seasonal data and fit a model to the data using sarima(). This time, the simulated data come from a mixed seasonal model, SARIMA(0,0,1)x(0,0,1)12. The plots on the right show three years of data, as well as the model ACF and PACF. Notice that, as opposed to the pure seasonal model, there are correlations at the nonseasonal lags as well as the seasonal lags.

## As always, the astsa package is preloaded. The generated data are in x.
## Instructions
##     Plot the sample ACF and PACF of the generated data to lag 60 (max.lag = 60) and compare them to the actual values.
##     Fit the model to generated data (x) using sarima(). As in the previous exercise, be sure to specify the additional seasonal arguments in your sarima() command.

# Plot sample P/ACF pair to lag 60 and compare to actual
acf2(x, max.lag = 60)

# Fit the seasonal model to x
sarima(x, p = 0, d = 0, q = 1, P = 0, D = 0, Q = 1, S = 12)

## Time series data collected on a seasonal basis typcially have mixed dependence. For example, what happens in June is often related to what happend in May as well as what happened in June of last year. 


##--
## Data Analysis - Unemployment I

## In the video, we fit a seasonal ARIMA model to the log of the monthly AirPassengers data set. You will now start to fit a seasonal ARIMA model to the monthly US unemployment data, unemp, from the astsa package.

## The first thing to do is to plot the data, notice the trend and the seasonal persistence. Then look at the detrended data and remove the seasonal persistence. After that, the fully differenced data should look stationary.

## The astsa package is preloaded in your workspace.
## Instructions

##     Plot the monthly US unemployment (unemp) time series from astsa. Note trend and seasonality.
##     Detrend and plot the data. Save this as d_unemp. Notice the seasonal persistence.
##     Seasonally difference the detrended series and save this as dd_unemp. Plot this new data and notice that it looks stationary now.

# Plot unemp 
plot(unemp)

# Difference your data and plot it
d_unemp <- diff(unemp)
plot(d_unemp)

# Seasonally difference d_unemp and plot it
dd_unemp <- diff(d_unemp, lag = 12)  


##--
## Data Analysis - Unemployment I

## In the video, we fit a seasonal ARIMA model to the log of the monthly AirPassengers data set. You will now start to fit a seasonal ARIMA model to the monthly US unemployment data, unemp, from the astsa package.

## The first thing to do is to plot the data, notice the trend and the seasonal persistence. Then look at the detrended data and remove the seasonal persistence. After that, the fully differenced data should look stationary.

## The astsa package is preloaded in your workspace.
## Instructions

##     Plot the monthly US unemployment (unemp) time series from astsa. Note trend and seasonality.
##     Detrend and plot the data. Save this as d_unemp. Notice the seasonal persistence.
##     Seasonally difference the detrended series and save this as dd_unemp. Plot this new data and notice that it looks stationary now.

# Plot unemp 
plot(unemp)

# Difference your data and plot it
d_unemp <- diff(unemp)
plot(d_unemp)

# Seasonally difference d_unemp and plot it
dd_unemp <- diff(d_unemp, lag = 12)  
plot(dd_unemp)


##--
## Data Analysis - Unemployment II

## Now, you will continue fitting an SARIMA model to the monthly US unemployment unemp time series by looking at the sample ACF and PACF of the fully differenced series.

## Note that the lag axis in the sample P/ACF plot is in terms of years. Thus, lags 1, 2, 3, ... represent 1 year (12 months), 2 years (24 months), 3 years (36 months), ...

## Once again, the astsa package is preloaded in your workspace.
## Instructions

##     Difference the data fully (as in the previous exercise) and plot the sample ACF and PACF of the transformed data to lag 60 months (5 years). Consider that, for
##         the nonseaonal component: the PACF cuts off at lag 2 and the ACF tails off.
##         the seasonal component: the ACF cuts off at lag 12 and the PACF tails off at lags 12, 24, 36, ...
##     Suggest and fit a model using sarima(). Check the residuals to ensure appropriate model fit.

# Plot P/ACF pair of fully differenced data to lag 60
dd_unemp <- diff(diff(unemp), lag = 12)
acf2(dd_unemp, max.lag = 60)

# Fit an appropriate model
sarima(unemp, p = 2, d = 1, q = 0, P = 0, D = 1, Q = 1, S = 12)


##--
## Data Analysis - Commodity Prices

## Making money in commodities is not easy. Most commodities traders lose money rather than make it. The package astsa includes the data set chicken, which is the monthly whole bird spot price, Georgia docks, US cents per pound, from August, 2001 to July, 2016.

## The astsa package is preloaded in your R console and the data are plotted for you, note the trend and seasonal components.

## First, you will use your skills to carefully fit an SARIMA model to the commodity. Later, you will use the fitted model to try and forecast the whole bird spot price.

## After removing the trend, the sample ACF and PACF suggest an AR(2) model because the PACF cuts off after lag 2 and the ACF tails off. However, the ACF has a small seasonal component remaining. This can be taken care of by fitting an addition SAR(1) component.

## By the way, if you are interested in analyzing other commodities from various regions, you can find many different time series at index mundi (http://www.indexmundi.com/commodities/).
## Instructions
##     Plot the differenced (d = 1) data diff(chicken). Note that the trend is removed and note the seasonal behavior.
##     Plot the sample ACF and PACF of the differenced data to lag 60 (5 years). Notice that an AR(2) seems appropriate but there is a small but significant seasonal component remaining in the detrended data.
##     Fit an ARIMA(2,1,0) to the chicken data to see that there is correlation remaining in the residuals.
##     Fit an SARIMA(2,1,0)x(1,0,0)12 and notice the model fits well.

# Plot differenced chicken
plot(diff(chicken))

# Plot P/ACF pair of differenced data to lag 60
acf2(diff(chicken), max.lag = 60)

# Fit ARIMA(2,1,0) to chicken - not so good
sarima(chicken, p = 2, d = 1, q = 0)

# Fit SARIMA(2,1,0,1,0,0,12) to chicken - that works
sarima(chicken, p = 2, d = 1, q = 0, P = 1, D = 0, Q = 0, S = 12)


##--
## Data Analysis - Birth Rate

## Now you will use your new skills to carefully fit an SARIMA model to the birth time series from astsa. The data are monthly live births (adjusted) in thousands for the United States, 1948-1979, and includes the baby boom after WWII.

## The birth data are plotted in your R console. Note the long-term trend (random walk) and the seasonal component of the data.
## Instructions

##     Use diff() to difference the data (d_birth). Use acf2() to view the sample ACF and PACF of this data to lag 60. Notice the seasonal persistence.
##     Use another call to diff() to take the seasonal difference of the data. Save this to dd_birth. Use another call to acf2() to view the ACF and PACF of this data, again to lag 60. Conclude that an SARIMA(0,1,1)x(0,1,1)12 model seems reasonable.
##     Fit the SARIMA(0,1,1)x(0,1,1)12 model. What happens?
##     Add an additional AR (nonseasonal, p = 1) parameter to account for additional correlation. Does the model fit well?

# Plot P/ACF to lag 60 of differenced data
d_birth <- diff(birth)
acf2(d_birth, max.lag=60)

# Plot P/ACF to lag 60 of seasonal differenced data
dd_birth <- diff(d_birth, lag = 12)
acf2(dd_birth, max.lag=60)

# Fit SARIMA(0,1,1)x(0,1,1)_12. What happens?
sarima(birth, p = 0, d = 1, q = 1, P = 0, D = 1, Q = 1, S = 12)

# Add AR term and conclude
sarima(birth, p = 1, d = 1, q = 1, P = 0, D = 1, Q = 1, S = 12)


##--
## Forecasting Monthly Unemployment

## Previously, you fit an SARIMA(2,1,0, 0,1,1)12 model to the monthly US unemployment time series unemp. You will now use that model to forecast the data 3 years.

## The unemp data are preloaded into your R workspace and plotted on the right.
## Instructions

##     Begin by again fitting the model used earlier in this chapter (using the sarima() command). Recheck the parameter significance and residual diagnostics.
##     Use sarima.for() to forecast the data 3 years into the future.

# Fit your previous model to unemp and check the diagnostics
sarima(unemp, p = 2, d = 1, q = 0, P = 0, D = 1, Q = 1, S = 12)

# Forecast the data 3 years into the future
sarima.for(unemp, n.ahead = 36, p = 2, d = 1, q = 0, P = 0, D = 1, Q = 1, S = 12)


##--
## How Hard is it to Forecast Commodity Prices?

## As previously mentioned, making money in commodities is not easy. To see a difficulty in predicting a commodity, you will forecast the price of chicken to five years in the future. When you complete your forecasts, you will note that even just a few years out, the acceptable range of prices is very large. This is because commodities are subject to many sources of variation.

## Recall that you previously fit an SARIMA(2,1,0, 1,0,0)12 model to the monthly US chicken price series chicken. You will use this model to calculate your forecasts.

## The astsa package is preloaded for you and the monthly price of chicken data (chicken) are plotted on the right.
## Instructions
##     Refit the SARIMA model from the earlier exercise and convince yourself that it fits well. Check parameter significance and residual diagnostics.
##     Use sarima.for() to forecast the data 5 years into the future.

# Fit the chicken model again and check diagnostics
sarima(chicken, p = 2, d = 1, q = 0, P = 1, D = 0, Q = 0, S = 12)

# Forecast the chicken data 5 years into the future
sarima.for(chicken, n.ahead = 60, p = 2, d = 1, q = 0, P = 1, D = 0, Q = 0, S = 12)

