## 1 - A quick introduction to base R graphics
##--
# Load MASS package
library(MASS)

# Plot whiteside data
plot(whiteside)

##--
# Plot Gas vs. Temp
plot(whiteside$Temp, whiteside$Gas,xlab='Outside temperature',ylab='Heating gas consumption')

##--
# Apply the plot() function to Insul
plot(whiteside$Insul)

##---
# Load the MASS package
library(MASS)

# Plot Max.Price vs. Price as red triangles
plot(Cars93$Price,Cars93$Max.Price,pch=17,col='red')

# Add Min.Price vs. Price as blue circles
points(Cars93$Price,Cars93$Min.Price, pch=16,col='blue')

# Add an equality reference line with abline()
abline(a = 0, b = 1, lty = 2)

##--
# Load the robustbase package
library(robustbase)

# Set up the side-by-side plot array
par(mfrow=c(1,2))

# First plot: brain vs. body in its original form
plot(Animals2$body,Animals2$brain)

# Add the first title
title("Original representation")

# Second plot: log-log plot of brain vs. body
plot(Animals2$body,Animals2$brain,log='xy')

# Add the second title
title('Log-log plot')

##--
# Load the insuranceData package
library(insuranceData)

# Use the data() function to get the dataCar data frame
data(dataCar)

# Set up a side-by-side plot array
par(mfrow=c(1,2))

# Create a table of veh_body record counts and sort
tbl <- sort(table(dataCar$veh_body), decreasing = TRUE)

# Create the pie chart and give it a title
pie(tbl)
title("Pie chart")

# Create the barplot with perpendicular, half-sized labels
barplot(tbl, las = 2, cex.names = 0.5)

# Add a title
title("Bar chart")



## 2 - Different plot types
##--
# Set up a side-by-side plot array
par(mfrow=c(1,2))

# Create a histogram of counts with hist()
hist(Cars93$Horsepower, main="hist() plot")

# Create a normalized histogram with truehist()
truehist(Cars93$Horsepower, main="truehist() plot")

##--
# Create index16, pointing to 16-week chicks
index16 <- which(ChickWeight$Time==16)

# Get the 16-week chick weights
weights <- ChickWeight$weight[index16]

# Plot the normalized histogram
truehist(weights)

# Add the density curve to the histogram
lines(density(weights))

##--
# Load the car package to make qqPlot() available
library(car)

# Create index16, pointing to 16-week chicks
index16 <- which(ChickWeight$Time==16)

# Get the 16-week chick weights
weights <- ChickWeight$weight[index16]

# Show the normal QQ-plot of the chick weights
qqPlot(weights)

# Show the normal QQ-plot of the Boston$tax data
qqPlot(Boston$tax)

##--
# Set up a side-by-side plot array
par(mfrow=c(1,2))

# Create the standard scatterplot
plot(Boston$zn, Boston$rad)

# Add the title
title("Standard scatterplot")

# Create the sunflowerplot
sunflowerplot(Boston$zn, Boston$rad)

# Add the title
title("Sunflower plot")

##--
# Create a variable-width boxplot with log y-axis & horizontal labels
boxplot(crim ~ rad, data=Boston, varwidth=TRUE,log='y',las=1)

# Add a title
title("Crime rate vs. radial highway index")

##--
## A mosaic plot may be viewed as a scatterplot between categorical variables
# Create a mosaic plot using the formula interface
mosaicplot(carb ~ cyl, data=mtcars)

##--
# Create a side-by-side boxplot summary
boxplot(Cars93$Min.Price, Cars93$Max.Price)

# Load aplpack to make the bagplot() function available
library(aplpack)

# Create a bagplot for the same two variables
bagplot(Cars93$Min.Price, Cars93$Max.Price, cex=1.2)

# Add an equality reference line
abline(a=0,b=1, lty=2)

##--
# Load the corrplot library for the corrplot() function
library(corrplot)

# Extract the numerical variables from UScereal
numericalVars <- UScereal[2:10]

# Compute the correlation matrix for these variables
corrMat <- cor(numericalVars)

# Generate the correlation ellipse plot
corrplot(corrMat, method='ellipse')

##--
# Load the rpart library
library(rpart)

# Fit an rpart model to predict medv from all other Boston variables
tree_model <- rpart(medv ~ ., data=Boston)

# Plot the structure of this decision tree model
plot(tree_model)

# Add labels to this plot
text(tree_model, cex=0.7)



## 3 - Adding details to plots
##--
# Assign the return value from the par() function to plot_pars
plot_pars <- par()

# Display the names of the par() function's list elements
names(plot_pars)

# Display the number of par() function list elements
length(plot_pars)

##--
# Set up a 2-by-2 plot array
par(mfrow=c(2,2))

# Plot the Animals2 brain weight data as points
plot(Animals2$brain, type="p")

# Add the title
title("points")

# Plot the brain weights with lines
plot(Animals2$brain, type="l")

# Add the title
title("lines")

# Plot the brain weights as lines overlaid with points
plot(Animals2$brain, type="o")

# Add the title
title("overlaid")

# Plot the brain weights as steps
plot(Animals2$brain, type="s")

# Add the title
title("steps")

##--
## The type = "n" option was discussed in the video and this exercise provides a simple example. This option is especially useful is when we are plotting data from multiple sources on a common set of axes. In such cases, we can compute ranges for the x- and y-axes so that all data points will appear on the plot, and then add the data with subsequent calls to points() or lines() as appropriate.

# Compute max_hp
max_hp <- max(Cars93$Horsepower, mtcars$hp)

# Compute max_mpg
max_mpg <- max(Cars93$MPG.city, Cars93$MPG.highway, mtcars$mpg)

# Create plot with type = "n"               
plot(max_hp, max_mpg,
     type = 'n', xlim = c(0, max_hp), ylim = c(0, max_mpg),
     xlab = 'Horsepower', ylab = 'Miles per gallon')

# Add open circles to plot
points(mtcars$hp, mtcars$mpg,  pch = 1)

# Add solid squares to plot
points(Cars93$Horsepower, Cars93$MPG.city, pch=15)

# Add open triangles to plot
points(Cars93$Horsepower, Cars93$MPG.highway, pch=6)

##--
# Create the numerical vector x
x <- seq(0, 10, length = 200)

# Compute the Gaussian density for x with mean 2 and standard deviation 0.2
gauss1 <- dnorm(x, mean = 2, sd = 0.2)

# Compute the Gaussian density with mean 4 and standard deviation 0.5
gauss2 <- dnorm(x, mean = 4, sd = 0.5)

# Plot the first Gaussian density
plot(x, gauss1, type='l', ylab='Gaussian probability density')

# Add lines for the second Gaussian density
lines(x, gauss2, lty=2, lwd=3)

##--
# Create an empty plot using type = "n"
plot(mtcars$hp, mtcars$mpg, xlab='Horsepower', ylab='Gas mileage', type='n')

# Add points with shapes determined by cylinder number
points(mtcars$hp, mtcars$mpg, pch = mtcars$cyl)

# Create a second empty plot
plot(mtcars$hp, mtcars$mpg, xlab='Horsepower', ylab='Gas mileage', type='n')

# Add points with shapes as cylinder characters
points(mtcars$hp, mtcars$mpg, pch = as.character(mtcars$cyl))

##--
# Build a linear regression model for the whiteside data
linear_model <- lm(Gas ~ Temp, data=whiteside)

# Create a Gas vs. Temp scatterplot from the whiteside data
plot(whiteside$Temp, whiteside$Gas)

# Use abline() to add the linear regression line
abline(linear_model, lty=2)

##--
# Create MPG.city vs. Horsepower plot with solid squares
plot(Cars93$Horsepower, Cars93$MPG.city, pch=15)

# Create index3, pointing to 3-cylinder cars
index3 <- which(Cars93$Cylinders==3)

# Add text giving names of cars next to data points
text(x = Cars93$Horsepower[index3], 
     y = Cars93$MPG.city[index3],
     labels = Cars93$Make[index3], adj = 0)

##--
# Plot MPG.city vs. Horsepower as open circles
plot(Cars93$Horsepower, Cars93$MPG.city, pch=1)

# Create index3, pointing to 3-cylinder cars
index3 <- which(Cars93$Cylinders==3)

# Highlight 3-cylinder cars as solid circles
points(Cars93$Horsepower[index3], Cars93$MPG.city[index3], pch=16)

# Add car names, offset from points, with larger bold text
text(Cars93$Horsepower[index3], Cars93$MPG.city[index3], label=Cars93$Make[index3], adj=-0.2, cex=1.2, font=4)

##--
# Plot Gas vs. Temp as solid triangles
plot(whiteside$Temp, whiteside$Gas, pch=17)

# Create indexB, pointing to "Before" data
indexB <- which(whiteside$Insul=='Before')

# Create indexA, pointing to "After" data
indexA <- which(whiteside$Insul=='After')

# Add "Before" text in blue, rotated 30 degrees, 80% size
text(x = whiteside$Temp[indexB], y = whiteside$Gas[indexB],
     labels = "Before", col = 'blue', srt = 30, cex = .8)

# Add "After" text in red, rotated -20 degrees, 80% size
text(x = whiteside$Temp[indexA], y = whiteside$Gas[indexA],
     labels = "After", col = 'red', srt = -20, cex = .8)

##--
# Set up and label empty plot of Gas vs. Temp
plot(whiteside$Temp, whiteside$Gas,
     type = 'n', xlab = "Outside temperature",
     ylab = "Heating gas consumption")

# Create indexB, pointing to "Before" data
indexB <- which(whiteside$Insul=='Before')

# Create indexA, pointing to "After" data
indexA <- which(whiteside$Insul=='After')

# Add "Before" data as solid triangles
points(whiteside$Temp[indexB], whiteside$Gas[indexB], pch=17)

# Add "After" data as open circles
points(whiteside$Temp[indexA], whiteside$Gas[indexA], pch=1)

# Add legend that identifies points as "Before" and "After"
legend("topright", pch = c(17,1), 
       legend = c('Before', 'After'))

##--
# Create a boxplot of sugars by shelf value, without axes
boxplot(sugars ~ shelf, data=UScereal, axes=FALSE)

# Add a default y-axis to the left of the boxplot
axis(side = 2)

# Add an x-axis below the plot, labelled 1, 2, and 3
axis(side = 1, at = c(1,2,3))

# Add a second x-axis above the plot
axis(side = 3, at = c(1,2,3),
     labels = c("floor", "middle", "top"))

##--
# Create a scatterplot of MPG.city vs. Horsepower
plot(Cars93$Horsepower, Cars93$MPG.city)

# Call supsmu() to generate a smooth trend curve, with default bass
trend1 <- supsmu(Cars93$Horsepower, Cars93$MPG.city)

# Add this trend curve to the plot
lines(trend1, lty=1)

# Call supsmu() for a second trend curve, with bass = 10
trend2 <- supsmu(Cars93$Horsepower, Cars93$MPG.city, bass=10)

# Add this trend curve as a heavy, dotted line
lines(trend2, lty=3, lwd=2)



## 4 - How much is too much?
##--
# Compute the number of plots to be displayed
ncol(Cars93)^2

# Plot the array of scatterplots
plot(Cars93)

##--
# Construct the vector keep_vars
keep_vars <- c("calories", "protein", "fat",
               "fibre", "carbo", "sugars")

# Use keep_vars to extract the desired subset of UScereal
df <- UScereal[, keep_vars]

# Set up a two-by-two plot array
par(mfrow=c(2,2))

# Use matplot() to generate an array of two scatterplots
matplot(UScereal$calories, UScereal[, c('protein', 'fat')],
        xlab="calories", ylab="")

# Add a title
title("Two scatterplots")

# Use matplot() to generate an array of three scatterplots
matplot(UScereal$calories, UScereal[, c('protein', 'fat', 'fibre')],
        xlab="calories", ylab="")

# Add a title
title("Three scatterplots")

# Use matplot() to generate an array of four scatterplots
matplot(UScereal$calories, UScereal[, c('protein', 'fat', 'fibre', 'carbo')],
        xlab="calories", ylab="")

# Add a title
title("Four scatterplots")

# Use matplot() to generate an array of five scatterplots
matplot(UScereal$calories, UScereal[, c('protein', 'fat', 'fibre', 'carbo', 'sugars')],
        xlab="calories", ylab="")

# Add a title
title("Five scatterplots")

##--
# Create mfr_table of manufacturer frequencies
mfr_table <- table(Cars93$Manufacturer)

# Create the default wordcloud from this table
wordcloud(words = names(mfr_table), 
          freq = as.numeric(mfr_table), 
          scale = c(2, 0.25))

# Change the minimum word frequency
wordcloud(words = names(mfr_table), 
          freq = as.numeric(mfr_table), 
          scale = c(2, 0.25), 
          min.freq = 1)

# Create model_table of model frequencies
model_table <- table(Cars93$Model)

# Create the wordcloud of all model names with smaller scaling
wordcloud(words = names(model_table), 
          freq = as.numeric(model_table), 
          scale = c(0.75, 0.25), 
          min.freq = 1)

##--
# Set up a two-by-two plot array
par(mfrow=c(2,2))

# Plot y1 vs. x1 
plot(anscombe$x1, anscombe$y1)

# Plot y2 vs. x2
plot(anscombe$x2, anscombe$y2)

# Plot y3 vs. x3
plot(anscombe$x3, anscombe$y3)

# Plot y4 vs. x4
plot(anscombe$x4, anscombe$y4)

##--
# Define common x and y limits for the four plots
xmin <- min(anscombe[c('x1', 'x2', 'x3', 'x4')])
xmax <- max(anscombe[c('x1', 'x2', 'x3', 'x4')])
ymin <- 3
ymax <- 13

# Set up a two-by-two plot array
par(mfrow=c(2,2))

# Plot y1 vs. x1 with common x and y limits, labels & title
plot(anscombe$x1, anscombe$y1,
     xlim = c(xmin, xmax),
     ylim = c(ymin, ymax),
     xlab = "x value", ylab = "y value",
     main = 'First dataset')

# Do the same for the y2 vs. x2 plot
plot(anscombe$x2, anscombe$y2,
     xlim = c(xmin, xmax),
     ylim = c(ymin, ymax),
     xlab = "x value", ylab = "y value",
     main = 'Second dataset')

# Do the same for the y3 vs. x3 plot
plot(anscombe$x3, anscombe$y3,
     xlim = c(xmin, xmax),
     ylim = c(ymin, ymax),
     xlab = "x value", ylab = "y value",
     main = 'Third dataset')

# Do the same for the y4 vs. x4 plot
plot(anscombe$x4, anscombe$y4,
     xlim = c(xmin, xmax),
     ylim = c(ymin, ymax),
     xlab = "x value", ylab = "y value",
     main = 'Fourth dataset')

##--
# Set up a two-by-two plot array
par(mfrow=c(2,2))

# Plot the raw duration data
plot(geyser$duration, main='Raw data')

# Plot the normalized histogram of the duration data
truehist(geyser$duration, main='Histogram')

# Plot the density of the duration data
plot(density(geyser$duration), main='Density')

# Construct the normal QQ-plot of the duration data
qqPlot(geyser$duration, main="QQ-plot")

##--
# Define row1, row2, row3 for plots 1, 2, and 3
row1 <- c(0, 1)
row2 <- c(2, 0)
row3 <- c(0, 3)

# Use the matrix function to combine these rows into a matrix
layoutMatrix <- matrix(c(row1, row2, row3), 
                       byrow = TRUE, nrow = 3)

# Call the layout() function to set up the plot array
layout(layoutMatrix)

# Show where the three plots will go 
layout.show(n=3)

##--
# Set up the plot array
layout(layoutMatrix)

# Construct vectors indexB and indexA
indexB <- which(whiteside$Insul=='Before')
indexA <- which(whiteside$Insul=='After')

# Create plot 1 and add title
plot(whiteside$Temp[indexB], whiteside$Gas[indexB], ylim = c(0,8))
title("Before data only")

# Create plot 2 and add title
plot(whiteside$Temp, whiteside$Gas, ylim = c(0,8))
title("Complete dataset")

# Create plot 3 and add title
plot(whiteside$Temp[indexA], whiteside$Gas[indexA], ylim = c(0,8))
title("After data only")

##--
# Create row1, row2, and layoutVector
row1 <- c(1,0,0)
row2 <- c(0,2,2)
layoutVector <- c(row1, row2, row2)

# Convert layoutVector into layoutMatrix
layoutMatrix <- matrix(layoutVector, byrow = TRUE, nrow = 3)

# Set up the plot array
layout(layoutMatrix)

# Plot scatterplot
plot(Boston$rad, Boston$zn)

# Plot sunflower plot
sunflowerplot(Boston$rad, Boston$zn)



## 5 - Advanced plot customization
##--
# Create a table of Cylinders frequencies
tbl <- table(Cars93$Cylinders)

# Generate a horizontal barplot of these frequencies. names.arg = "" to suppress the y-axis legend.
mids <- barplot(tbl, horiz = TRUE,
                col = "transparent",
                names.arg = "")

# Add names labels with text()
text(20, mids, labels=names(tbl))

# Add count labels with text()
text(35, mids, as.numeric(tbl))

##--
# Call symbols() to create the default bubbleplot
symbols(Cars93$Horsepower, Cars93$MPG.city, circles = Cars93$Cylinders)

# Repeat, with the inches argument specified
symbols(Cars93$Horsepower, Cars93$MPG.city, circles = Cars93$Cylinders,
        inches = 0.2)

##--
# Call png() with the name of the file we want to create
png("bubbleplot.png")

# Re-create the plot from the last exercise
symbols(Cars93$Horsepower, Cars93$MPG.city,
        circles = Cars93$Cylinders,
        inches = 0.2)

# Save our file and return to our interactive session
dev.off()

# Verify that we have created the file
list.files(pattern = "png")

##--
# Iliinsky and Steele color name vector
IScolors <- c("red", "green", "yellow", "blue",
              "black", "white", "pink", "cyan",
              "gray", "orange", "brown", "purple")

# Create the data for the barplot
barWidths <- c(rep(2, 6), rep(1, 6))

# Recreate the horizontal barplot with colored bars
barplot(rev(barWidths), horiz = TRUE,
        col = rev(IScolors), axes = FALSE,
        names.arg = rev(IScolors), las = 1)

##--
# Iliinsky and Steele color name vector
IScolors <- c("red", "green", "yellow", "blue",
              "black", "white", "pink", "cyan",
              "gray", "orange", "brown", "purple")

# Create the colored bubbleplot
symbols(Cars93$Horsepower, Cars93$MPG.city, 
        circles = Cars93$Cylinders, inches = 0.2, 
        bg = IScolors[Cars93$Cylinders])

##--
# Create a table of Cylinders by Origin
tbl <- table(Cars93$Cylinders, grouping=Cars93$Origin)

# Create the default stacked barplot
barplot(tbl)

# Enhance this plot with color
barplot(tbl, col=IScolors)

##--
# Load the insuranceData package
library(insuranceData)

# Use the data() function to load the dataCar data frame
data(dataCar)

# Load the tabplot package
suppressPackageStartupMessages(library(tabplot))

# Generate the default tableplot() display
tableplot(dataCar)

##--
# Load the lattice package
library(lattice)

# Use xyplot() to construct the conditional scatterplot
xyplot(calories ~ sugars | shelf, data=UScereal)

##-
# Load the ggplot2 package
library(ggplot2)

# Create the basic plot (not displayed): basePlot
basePlot <- ggplot(Cars93, aes(x = Horsepower, y = MPG.city))

# Display the basic scatterplot
basePlot + geom_point()

# Color the points by Cylinders value
basePlot + geom_point(colour = IScolors[Cars93$Cylinders])

# Make the point sizes also vary with Cylinders value
basePlot + geom_point(colour = IScolors[Cars93$Cylinders], size = as.numeric(Cars93$Cylinders))
