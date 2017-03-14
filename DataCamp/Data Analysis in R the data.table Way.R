## 1 - Data.table novice

##--
## Create and subset a data.table

## Welcome to the interactive exercises for your data.table course. Here you will learn the ins and outs of working with the data.table package.

## While most of the material is covered by Matt and Arun in the videos, you will sometimes need to show some street smarts to get to the right answer. Remember that before using the hint you can always have a look at the official documentation by typing ?data.table in the console.

## Let's start with some warm-up exercises based on the topics covered in the video. Recall from the video that you can use L after a numeric to specify that it is an integer. You can also give columns with different lengths when creating a data.table, and R will "recycle" the shorter column to match the length of the longer one by re-using the first items. In the example below, column x is recycled to match the length of column y:

## data.table(x = c("A", "B"), y = 1:4)
##    x y
## 1: A 1
## 2: B 2
## 3: A 3
## 4: B 4

## You can also review the slides used in the videos by pressing the slides button.
## Instructions

##     Create a data.table my_first_data_table with a column x = c("a", "b", "c", "d", "e") and a column y = c(1, 2, 3, 4, 5). Use the function data.table().
##     Create a two-column data.table DT that contains the four integers 1, 2, 1 and 2 in the first column a and the letters A, B, C and D in the second column b. Use recycling so that the contents of a will be automatically used twice. Note that LETTERS[1] returns "A", LETTERS[2] returns "B", and so on.
##     Select the third row of DT and just print the result to the console.
##     Select the second and third rows without using commas and print the result to the console.

# The data.table package is preloaded

# Create my_first_data_table
my_first_data_table <- data.table(x = c("a", "b", "c", "d", "e"), 
                                  y = c(1, 2, 3, 4, 5))  
  
# Create a data.table using recycling
DT <- data.table(a = c(1L, 2L), b = LETTERS[1:4])

# Print the third row to the console
DT[3]

# Print the second and third row to the console without using commas
DT[2:3]


##--
## Getting to know a data.table

## You can pass a data.table to base R functions like head() and tail() that accept a data.frame because data.tables are also data.frames. Also, keep in mind that the special symbol .N, when used inside square brackets, contains the number of rows. For example, DT[.N] and DT[nrow(DT)] will both return the last row in DT.
## Instructions

##     Select the second to last row of the table using .N.
##     Return the column names() of the data.table.
##     Return the number of rows and number of columns of the data.table using the dim() function.
##     Select row 2 twice and row 3 once, returning a data.table with three rows (two of which are identical).

# DT and the data.table package are pre-loaded

# Print the second to last row of DT using .N
DT[.N - 1]

# Print the column names of DT
colnames(DT)

# Print the number or rows and columns of DT
dim(DT)

# Print a new data.table containing rows 2, 2, and 3 of DT
DT[c(2, 2, 3)]


##--
## Subsetting data.tables

## As a reminder, DT[i, j, by] is pronounced

## Take DT, subset rows using i, then calculate j grouped by by.

## In the video, the second argument j was covered. j can be used to select columns by wrapping the column names in .().

## In addition to selecting columns, you can also call functions on them as if the columns were variables. For example, if you had a data.table heights storing people's heights in inches, you could compute their heights in feet as follows:

##     name  eye_color   height_inch
## 1:   Tom      Brown            69
## 2: Boris       Blue            71
## 3:   Jim       Blue            68

## > heights[, .(name, 
##               height_ft = height_inch / 12)]
##     name   height_ft
## 1:   Tom    5.750000
## 2: Boris    5.916667
## 3:   Jim    5.666667

## Instructions

##     Create a subset containing the columns B and C for rows 1 and 3 of DT. Simply print out this subset to the console.
##     From DT, create a data.table, ans with two columns: B and val, where val is the product of A and C.
##     Fill in the blanks in the assignment of ans2, such that it equals the data.table specified in target. Use columns from the previously defined data.tables to produce the val column.

# DT and the data.table package are pre-loaded

# Subset rows 1 and 3, and columns B and C
DT[c(1, 3), .(B, C)]

# Assign to ans the correct value
ans <- DT[, .(B, val = A * C)]

# Fill in the blanks such that ans2 equals target
target <- data.table(B = c("a", "b", "c", "d", "e", 
                           "a", "b", "c", "d", "e"), 
                     val = as.integer(c(6:10, 1:5)))

ans2 <- DT[, .(B, val = c(C, A))]


##--
## The by basics

## In this section you were introduced to the last of the main parts of the data.table syntax: by. If you supply a j expression and a by list of expressions, the j expression is repeated for each by group. Time to master the by argument with some hands-on examples and exercises.

## First, just print iris to the console and observe that all rows are printed and that the column names scroll off the top of your screen. This is because iris is a data.frame. Scroll back up to the top to see the column names.
## Instructions

##     Convert the iris dataset to a data.table DT. You're now ready to use data.table magic on it!
##     Create a new column containing the mean Sepal.Length for each Species. Do not provide a name for this newly created column.
##     Do exactly the same as in the instruction above, but this time, group by the first letter of the Species name instead. Use substr() for this.

# iris is already available in your workspace

# Convert iris to a data.table: DT
DT <- as.data.table(iris)

# For each Species, print the mean Sepal.Length
DT[, mean(Sepal.Length), by = Species]

# Print mean Sepal.Length, grouping by first letter of Species
DT[, mean(Sepal.Length), by = substr(Species, 1, 1)]


##--
## Using .N and by

## You saw earlier that .N can be used in i and that it designates the number of rows in DT. There, it is typically used for returning the last row or an offset from it. .N can be used in j too and designates the number of rows in this group. This becomes very powerful when you use it in combination with by.

## DT, a data.table version of iris, is already loaded in your workspace, so you can start experimenting right away. In this exercise, you will group by sepal area. Though sepals aren't rectangles, just multiply the length by the width to calculate the area.
## Instructions

##     Group the specimens by Sepal area (Sepal.Length * Sepal.Width) to the nearest 10 cm2

## . Count how many occur in each group by specifying .N in j. Simply print the resulting data.table. Use the template in the sample code by filling in the blanks.
## Copy and adapt the solution to the above question, to name the columns Area and Count, respectively.

# data.table version of iris: DT
DT <- as.data.table(iris)

# Group the specimens by Sepal area (to the nearest 10 cm2) and count how many occur in each group.
DT[, .N, by = 10 * round(Sepal.Length * Sepal.Width / 10)]

# Now name the output columns `Area` and `Count`
DT[, .(Count = .N), by = .(Area = 10 * round(Sepal.Length * Sepal.Width / 10))]


##--
## Return multiple numbers in j

## In the previous exercises, you've returned only single numbers in j. However, this is not necessary. You'll experiment with this via a new data.table DT, which has already been specified in the sample code.
## Instructions

##     Create a new data.table DT2 with 3 columns, A, B and C, where C is the cumulative sum of the C column of DT. Call the cumsum() function in the j argument, and group by .(A, B) (i.e. both columns A and B).
##     Select from DT2 the last two values of C using the tail() function, and assign that to column C while you group by A alone. Make sure the column names don't change.

# Create the data.table DT
DT <- data.table(A = rep(letters[2:1], each = 4L), 
                 B = rep(1:4, each = 2L), 
                 C = sample(8))

# Create the new data.table, DT2
DT2 <- DT[, .(C = cumsum(C)), by = .(A, B)]

# Select from DT2 the last two values from C while you group by A
DT2[, .(C = tail(C, 2)), by = A]




## 2 - Data.table yeoman
##--
## Chaining, the basics

## Now that you are comfortable with data.table's DT[i, j, by] syntax, it is time to practice some other very useful concepts in data.table. Here, we'll have a more detailed look at chaining.

## Chaining allows the concatenation of multiple operations in a single expression. It's easy to read because the operations are carried out from left to right. Furthermore, it helps to avoid the creation of unnecessary temporary variables (which could quickly clutter one's workspace).
## Instructions

## In the previous section, you calculated DT2 by taking the cumulative sum of C while grouping by A and B. Next, you selected the last two values of C from DT2 while grouping by A alone. This code is included in the sample code. Use chaining to restructure the code. Simply print out the result of chaining.

# The data.table package has already been loaded

# Build DT
DT <- data.table(A = rep(letters[2:1], each = 4L), 
                 B = rep(1:4, each = 2L), 
                 C = sample(8)) 

# Combine the two steps in a one-liner
DT[, .(C = cumsum(C)), by = .(A, B)][, .(C = tail(C, 2)), by = A]

##--
## Chaining your iris dataset

## In the previous chapter, you converted the iris dataset to a data.table DT. This DT is already available in your workspace. Print DT to the console to remind yourself of its contents. Now, let's see how you can use chaining to simplify manipulations and calculations.
## Instructions

## Get the median of each of the four columns Sepal.Length, Sepal.Width, Petal.Length and Petal.Width, while grouping by Species. Reuse the same column names (e.g. the column containing the median Sepal.Length is still called Sepal.Length). Next, order() Species in descending order using chaining. This is deliberately repetitive, but we have a solution for you in the next exercise!

# The data.table DT is loaded in your workspace

# Perform chained operations on DT
DT[, .(Sepal.Length = median(Sepal.Length), 
       Sepal.Width = median(Sepal.Width), 
       Petal.Length = median(Petal.Length),
       Petal.Width = median(Petal.Width)), 
   by = Species][order(-Species)]


##--
## Programming time vs readability

## It is a good idea to make use of familiar functions from base R to reduce programming time without losing readability.

## The data.table package provides a special built-in variable .SD. It refers to the subset of data for each unique value of the by argument. That is, the number of observations in the output will be equal to the number of unique values in by.

## Recall that the by argument allows us to separate a data.table into groups. We can now use the .SD variable to reference each group and apply functions separately. For example, suppose we had a data.table storing information about dogs:
## Sex 	Weight 	Age 	Height
## M 	40 	1 	12
## F 	30 	4 	7
## F 	80 	12 	9
## M 	90 	3 	14
## M 	40 	6 	12

## We could then use

## dogs[, lapply(.SD, mean), by = Sex]

## to produce average weights, ages, and heights for male and female dogs separately:

##    Sex   Weight      Age   Height
## 1:   M 56.66667 3.333333 12.66667
## 2:   F 55.00000 8.000000  8.00000

## A data.table DT has been created for you and is available in the workspace. Type DT in the console to print it out and inspect it.
## Instructions

##     Get the mean of columns y and z grouped by x by using .SD.
##     Get the median of columns y and z grouped by x by using .SD.

# A new data.table DT is available

# Mean of columns
DT[, lapply(.SD, mean), by = x]

# Median of columns
DT[, lapply(.SD, median), by = x]


##--
## Introducing .SDcols

## .SDcols specifies the columns of DT that are included in .SD. Using .SDcols comes in handy if you have too many columns and you want to perform a particular operation on a subset of the columns (apart from the grouping variable columns).

## Using .SDcols allows you to apply a function to all rows of a data.table, but only to some of the columns. For example, consider the dog example from the last exercise. If you wanted to compute the average weight and age (the second and third columns) for all dogs, you could assign .SDcols accordingly:

## dogs[, lapply(.SD, mean), .SDcols = 2:3]
##    Weight Age
## 1:     56 5.2

## While learning the data.table package, you may want to occasionally refer to the documentation. Have a look at ?data.table for more info on .SDcols.

## Yet another data.table, DT, has been prepared for you in your workspace. Start by printing it to the console.
## Instructions

##     Calculate the sum of the columns that start with Q, using .SD and .SDcols. Set .SDcols equal to 2:4.
##     Set .SDcols to be the result of a function call. This time, calculate the sum of columns H1 and H2 using paste0() to specify the .SDcols argument.
##     Finally, select all but the first row of the groups names 6 and 8, returning only the grp column and the columns that start with Q. Use -1 in i of .SD and use paste0() again. Type desired_result into the console to see what your answer should look like.

# A new data.table DT is available

# Calculate the sum of the Q columns
DT[, lapply(.SD, sum), .SDcols = 2:4]

# Calculate the sum of columns H1 and H2 
DT[, lapply(.SD, sum), .SDcols = paste0("H", 1:2)]

# Select all but the first row of groups 1 and 2, returning only the grp column and the Q columns
DT[, .SD[-1], by = grp, .SDcols = paste0("Q", 1:3)]


##--
## Mixing it together: lapply, .SD, .SDcols and .N

## This exercise is a challenging one, so don't give up! It's important to remember that whenever the j argument is a list (e.g. if it contains .SD or a call to lapply()), a data.table is returned. For example:

## dogs[, lapply(.SD, mean), by = sex, .SDcols = c("weight", "age")]

## will return a data.table containing average weights and ages for dogs of each sex.

## It's also helpful to know that combining a list with a vector results in a new longer list. Lastly, note that when you select .N on its own, it is renamed N in the output for convenience when chaining.

## For this exercise, DT, which contains variables x, y, and z, is loaded in your workspace. You must combine lapply(), .SD, .SDcols, and .N to get your call to return a specific output. Good luck!
## Instructions

##     Get the sum of all columns x, y and z and the number of rows in each group while grouping by x. Your answer should be identical to this:

##      x x  y  z N
##   1: 2 8 26 30 4
##   2: 1 3 23 26 3

##     Get the cumulative sum of column x and y while grouping by x and z > 8 such that the answer looks like this:

##      by1   by2 x  y
##   1:   2 FALSE 2  1
##   2:   2 FALSE 4  6
##   3:   1 FALSE 1  3
##   4:   1 FALSE 2 10
##   5:   2  TRUE 2  9
##   6:   2  TRUE 4 20
##   7:   1  TRUE 1 13

# DT is pre-loaded

# Sum of all columns and the number of rows
DT[, c(lapply(.SD, sum), .N), by = x, .SDcols = c("x", "y", "z")]

# Cumulative sum of column x and y while grouping by x and z > 8
DT[, lapply(.SD, cumsum), by = .(by1 = x, by2 = z > 8), .SDcols = c("x", "y")]


##--
## Adding, updating and removing columns

## As you now know, := is defined for use in j only, and is used to update data.tables by reference. One way of using := is the LHS := RHS form, where LHS is a character vector of columns (referenced by name or number) you wish to update and RHS is the corresponding value for each column (Note: LHS stands for "left hand side" and RHS stands for "right hand side" in what follows).

## For example, the following line multiplies every row of column C by 10 and stores the result in C:

## DT[, C := C * 10]

## This first exercise will thoroughly test your understanding of := used in the LHS := RHS form. It's time for you to show off your knowledge! A data.table DT has been defined for you in the sample code.
## Instructions

##     Add a column to DT by reference, named Total, that contains sum(B) for each group in column A.
##     Add 1L to the values in column B, but only in the rows 2 and 4.
##     Add a new column Total2 that contains sum(B) grouped by A but just over rows 2, 3 and 4.
##     Remove the Total column from DT.
##     Use [[ to select the third column as a vector. Simply print it out to the console.

# The data.table DT
DT <- data.table(A = letters[c(1, 1, 1, 2, 2)], B = 1:5)

# Add column by reference: Total
DT[, Total := sum(B), by = A]

# Add 1 to column B
DT[c(2, 4), B := B + 1L]

# Add a new column Total2
DT[2:4, Total2 := sum(B), by = A]

# Remove the Total column
DT[, Total := NULL]

# Select the third column using `[[`
DT[[3]]


##--
## The functional form

## You've had practice with using := in the LHS := RHS form. The second way to use := is with functional form:

## DT[, `:=`(colA = colB + colC)]

## Notice that the := is surrounded by two tick marks! Otherwise data.table will throw a syntax error. It is also important to note that in the generic functional form above, my_fun() can refer to any function, including the basic arithmetic functions. The nice thing about the functional form is that you can get both the RHS alongside the LHS so that it's easier to read.

## Time for some experimentation. A data.table DT has been prepared for you in the sample code.
## Instructions

##     Update B with B + 1, add a new column C with A + B, and add a new column D of just 2's.
##     A variable my_cols has already been defined. Use it to delete these columns from DT.
##     Finally, delete column D using the column number (2), not its name (D).

# A data.table DT has been created for you
DT <- data.table(A = c(1, 1, 1, 2, 2), B = 1:5)

# Update B, add C and D
DT[, `:=`(B = B + 1, C = A + B, D = 2)]

# Delete my_cols
my_cols <- c("B", "C")
DT[, (my_cols) := NULL]

# Delete column 2 by number
DT[, 2 := NULL]


##--
## Ready, set(), go!

## The set() function is used to repeatedly update a data.table by reference. You can think of the set() function as a loopable, low overhead version of the := operator, except that set() cannot be used for grouping operations. The structure of the set() function looks like this:

## set(DT, index, column, value)

## The function takes four arguments:

##     A data.table with the columns you wish to update
##     The index used in a loop (e.g. the i in for(i in 1:5))
##     The column or columns you wish to update in the loop
##     How the column or columns should be updated

## In the next two exercises, you will focus on using set() and its siblings setnames() and setcolorder(). You are two exercises away from becoming a data.table yeoman!
## Instructions

##     A data.table DT has been created for you in the workspace. Check it out!
##     Loop through columns 2, 3, and 4, and for each one, select 3 rows at random and set the value of that column to NA.
##     Change the column names to lower case using the tolower() function. When setnames() is passed a single input vector, that vector needs to contain all the new names.
##     Print the resulting DT to the console to see what changed.

# Set the seed
set.seed(1)

# Check the DT that is made available to you
DT

# For loop with set
for (i in 2:4) set(DT, sample(10, 3), i, NA)

# Change the column names to lowercase
setnames(DT, tolower(names(DT)))

# Print the resulting DT to the console
DT


##--
## The set() family

## A summary of the set() family:

##     set() is a loopable, low overhead version of :=.
##     You can use setnames() to set or change column names.
##     setcolorder() lets you reorder the columns of a data.table.

## A data.table DT has been defined for you in the sample code.
## Instructions

##     First, add a suffix "_2" to all column names of DT. Use paste0() here.
##     Next, use setnames() to change a_2 to A2.
##     Lastly, reverse the order of the columns with setcolorder().

# Define DT
DT <- data.table(a = letters[c(1, 1, 1, 2, 2)], b = 1)

# Add the suffix "_2" to all column names
setnames(DT, paste0(names(DT), "_2"))

# Change column name a_2 to A2
setnames(DT, "a_2", "A2")

# Reverse the order of the columns
setcolorder(DT, c("b_2", "A2"))

# Alternative solution using column numbers
# setcolorder(DT, 2:1)


##--
## Selecting rows the data.table way

## In the video, Matt showed you how to use column names in i to select certain rows. Since practice makes perfect, and since you will find yourself selecting rows over and over again, it'll be good to do a small exercise on this with the familiar iris dataset.
## Instructions

##     Convert the iris dataset to a data.table and store the result as iris.
##     Select all the rows where Species is "virginica".
##     Select all the rows where Species is either "virginica" or "versicolor".

# The data.table package is pre-loaded

# Convert iris to a data.table
iris <- as.data.table(iris)

# Species is "virginica"
iris[Species == "virginica"]

# Species is either "virginica" or "versicolor"
iris[Species %in% c("virginica","versicolor")]


##--
## Removing columns and adapting your column names

## In the previous exercise, you selected certain rows from the iris data.table based on the column names. Now you have to take your understanding of the data.table package to the next level by using standard R functions and regular expressions to remove columns and change column names. To practice this, you'll do a little manipulation to prepare for the next exercise.

## Since regular expressions can be tricky, here is a quick refresher:

##     Metacharacters allow you to match certain types of characters. For example, . means any single character, ^ means "begins with", and $ means "ends with".
##     If you want to use any of the metacharacters as actual text, you need to use the \\ escape sequence.

## Instructions

##     Simplify the names of the columns in iris that contain "Sepal." by removing the "Sepal." prefix. Use gsub() along with the appropriate regular expression inside a call to setnames().
##     Remove the two columns that start with "Petal" from the iris data.table.

# iris as a data.table
iris <- as.data.table(iris)

# Remove the "Sepal." prefix
setnames(iris, gsub("^Sepal\\.", "", names(iris)))

# Remove the two columns starting with "Petal"
iris[, grep("^Petal", names(iris)) := NULL]


##--
## Understanding automatic indexing

## You've been introduced to the rule that "if i is a single variable name, it is evaluated in the calling scope, otherwise inside DT's scope". This is a very important rule if you want to conceptually understand what is going on when using column names in i. Only single columns on the left side of operators benefit from automatic indexing.

## The iris data.table with the variable names you updated in the previous exercise is available in your workspace.
## Instructions

##     Select the rows where the area is greater than 20 square centimeters.
##     Add a new boolean column containing Width * Length > 25 and call it is_large. Remember that := can be used to create new columns.
##     Select the rows for which the value of is_large is TRUE.

# Cleaned up iris data.table
iris

# Area is greater than 20 square centimeters
iris[ Width * Length > 20 ]

# Add new boolean column
iris[, is_large := Width * Length > 25]

# Now large observations with is_large
iris[is_large == TRUE]
iris[(is_large)] # Also OK


##--
## Selecting groups or parts of groups

## The previous exercise illustrated how you can manually set a key via setkey(DT, A, B). setkey() sorts the data by the columns that you specify and changes the table by reference. Having set a key will allow you to use it, for example, as a super-charged row name when doing selections. Arguments like mult and nomatch then help you to select only particular parts of groups.

## Furthermore, two of the instructions will require you to make use of by = .EACHI. This allows you to run j for each group in which each item in i joins too. The last instruction will require you to produce a side effect inside the j argument in addition to selecting rows.
## Instructions

## A data.table DT has already been created for you with the keys set to A and B.

##     Select the "b" group without using ==.
##     Select the "b" and "c" groups, again without using ==.
##     Select the first row of the "b" and "c" groups using mult.
##     Use by = .EACHI and .SD to select the first and last row of the "b" and "c" groups.
##     Extend the previous command to print out the group before returning the first and last row from it. You can use curly brackets to include two separate instructions inside the j argument.

# The 'keyed' data.table DT
DT <- data.table(A = letters[c(2, 1, 2, 3, 1, 2, 3)], 
                 B = c(5, 4, 1, 9, 8, 8, 6), 
                 C = 6:12)
setkey(DT, A, B)

# Select the "b" group
DT["b"]

# "b" and "c" groups
DT[c("b", "c")]

# The first row of the "b" and "c" groups
DT[c("b", "c"), mult = "first"]

# First and last row of the "b" and "c" groups
DT[c("b", "c"), .SD[c(1, .N)], by = .EACHI]

# Copy and extend code for instruction 4: add printout
DT[c("b", "c"), { print(.SD); .SD[c(1, .N)] }, by = .EACHI]


##--
## Rolling joins - part one

## In the last video, you learned about rolling joins. The roll applies to the NA values in the last join column. In the next three exercises, you will learn how to work with rolling joins in a data.table setting.
## Instructions

## The same keyed data.table from before, DT, has been provided in the sample code.

##     Get the key of DT through the key() function.
##     Use the super-charged row names to look up the row where A == "b" and B == 6, without using ==! Verify here that column C is NA.
##     Based on the query that was written in the previous instruction, return the prevailing row before this "gap". Specify the roll argument.
##     Again, start with the code from the second instruction, but this time, find the nearest row. Specify the roll argument accordingly.

# Keyed data.table DT
DT <- data.table(A = letters[c(2, 1, 2, 3, 1, 2, 3)], 
                 B = c(5, 4, 1, 9, 8, 8, 6), 
                 C = 6:12, 
                 key = "A,B")

# Get the key of DT
key(DT)

# Row where A == "b" and B == 6
DT[.("b", 6)]

# Return the prevailing row
DT[.("b", 6), roll = TRUE]

# Return the nearest row
DT[.("b", 6), roll = "nearest"]


##--
## Rolling joins - part two

## It is time to move on to the rollends argument. The rollends argument is actually a vector of two logical values, but remember that you can always look this up via ?data.table. You were introduced to this argument via the control ends section. If you want to roll for a certain distance, you should continue to use the roll argument.
## Instructions

##     For the group where column A is equal to "b", print out the sequence when column B is set equal to (-2):10. Remember, A and B are the keys for this data.table.
##     Extend the code you wrote for the first instruction to roll the prevailing values forward to replace the NAs.
##     Extend your code with the appropriate rollends value to roll the first observation backwards.

# Keyed data.table DT
DT <- data.table(A = letters[c(2, 1, 2, 3, 1, 2, 3)], 
                 B = c(5, 4, 1, 9, 8, 8, 6), 
                 C = 6:12, 
                 key = "A,B")

# Print the sequence (-2):10 for the "b" group
DT[.("b", (-2):10)]

# Add code: carry the prevailing values forwards
DT[.("b", (-2):10), roll = TRUE]

# Add code: carry the first observation backwards
DT[.("b", (-2):10), roll = TRUE, rollends = TRUE]
DT[.("b", (-2):10), roll = TRUE, rollends = c(TRUE, TRUE)] # also OK


