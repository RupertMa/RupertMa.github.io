---
layout: post
---

# R notes | R语言笔记
## data.table
```R
tab = data.table(a= c(1,2,3,4),
                 b= c('a','b','c','d'),
                 c= c('2018-01-01','2018-01-01','2018-01-01','2018-01-01'))
tab_l = data.table(a= list(1,2,3,4),
                 b= c('a','b','c','d'),
                 c= c('2018-01-01','2018-01-01','2018-01-01','2018-01-01'))
```

The second one makes tab_l$a a compound object and then some operations don't work on it. See examples below:

```R
tab[, ':=' (d = mean(a),
           e = sum(a))]

tab_l[, ':=' (d = mean(a),
           e = sum(a))]
```
This assigning operation doesn't work if tab$a is a list.  

So convert tab$a to a vector by:
```R
tab_l[, a:= sapply(a, as.vector)]

tab_l[, ':=' (d = mean(a),
           e = sum(a))]
```

More examples about data.table
```R
# Create a new table
tab[, .(f = mean(a), g = sum(a))]

# Change columns' data types
# 1. Change all columns to one type
tab[, lapply(.SD, as.character)] # Return a new dt
tab[, lapply(.SD, class)]

# 2. Change some columns to one type
convcols= c('a','b','c','d') # Return a new dt
tab[,lapply(.SD,as.character),.SDcols=convcols]

# 3. Change any columns to one type inplace
for (col in convcols) set(tab, j=col, value=as.character(tab[[col]]))
tab[, lapply(.SD, class)]


```