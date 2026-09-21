0:01
So, you've learned about gradient descent, about multiple linear regression, and also vectorization.
0:07
Let's put it all together to implement gradient descent for multiple linear regression with vectorization. This would be cool.
0:14
Let's quickly review what multiple linear regression looks like.
0:17
Using our previous notation, let's see how you can write it more succinctly using vector notation.
0:23
We have parameters w1 to wn as well as b, but instead of thinking of w1 to wn as separate numbers, that is, separate parameters,
0:34
let's instead collect all of the w's into a vector w, so that now w is a vector of length n.
0:43
So, we're just going to think of the parameters of this model as a vector w, as well as b, where b is still a number, same as before.
0:53
Whereas before, we had defined multiple linear regression like this, now, using vector notation,
1:00
we can write the model as f sub wb of x equals the vector w dot product with the vector x plus b.
1:09
And remember that this dot here means dot product.
1:14
Our cost function can be defined as j of w1 through wn comma b,
1:20
but instead of just thinking of j as a function of these n different parameters wj as well as b,
1:28
we're going to write j as a function of parameter vector w and the number b.
1:35
So, this w1 through wn is replaced by this vector w, and j now takes its input, a vector w and a number b, and returns a number.
1:49
Here's what gradient descent looks like.
1:51
We're going to repeatedly update each parameter wj to be wj minus alpha times the derivative of the cost j,
2:00
where j has parameters w1 through wn and b, and once again, we just write this as j of vector w and number b.
2:12
Let's see what this will look like when you implement gradient descent, and in particular, let's take a look at the derivative term.
2:20
We'll see that gradient descent becomes just a little bit different with multiple features compared to just one feature.
2:28
Here's what we had when we had gradient descent with one feature.
2:32
We had an update rule for w and a separate update rule for b, so hopefully these look familiar to you.
2:40
And this term here is the derivative of the cost function j with respect to the parameter w,
2:48
and similarly, we have an update rule for parameter b with univariate regression.
2:54
We had only one feature.
2:56
We call that feature xi without any subscript.
3:01
Now, here's the new notation for when we have n features where n is 2 or more.
3:08
We get this update rule for gradient descent.
3:11
Update w1 to be w1 minus alpha times this expression here, and this formula is actually the derivative of the cost j with respect to w1.
3:26
The formula for the derivative of j with respect to w1 on the right looks very similar to the case of one feature on the left.
3:35
The error term still takes a prediction f of x minus the target y.
3:41
One difference is that w and x are now vectors, and just as w on the left has now become w1 here on the right,
3:51
xi here on the left is now instead xi subscript 1 here on the right, and this is just for j equals 1.
4:03
For multiple linear regression, we have j ranging from 1 through n, and so we'll update the parameters w1, w2 all the way up to wn,
4:18
and then as before, we'll update b, and if you implement this, you get gradient descent for multiple regression.
4:28
So that's it for gradient descent for multiple regression.
4:33
Before moving on from this video, I want to make a quick aside or a quick side note on an alternative way for finding w and b for linear regression,
4:46
and this method is called the normal equation.
4:50
Whereas it turns out gradient descent is a great method for minimizing the cost function j to find w and b,
4:58
there is one other algorithm that works only for linear regression and pretty much none of the other algorithms you see in this specialization for solving for w and b,
5:09
and this other method does not need an iterative gradient descent algorithm.
5:14
Called the normal equation method, it turns out to be possible to use an advanced linear algebra library to just solve for w and b all in one go without iterations.
5:25
Some disadvantages of the normal equation method are, first, unlike gradient descent, this does not generalize to other learning algorithms,
5:34
such as the logistic regression algorithm that you learn about next week or the neural networks or other algorithms you see later in this specialization.
5:43
The normal equation method is also quite slow if the number of features n is large.
5:49
Almost no machine learning practitioners should implement the normal equation method themselves,
5:55
but if you are using a mature machine learning library and call linear regression, there is a chance that on the back end you will be using this to solve for w and b.
6:07
So if you are ever in a job interview and hear the term normal equation, that's what this refers to.
6:13
Don't worry about the details of how the normal equation works.
6:17
Just be aware that some machine learning libraries may use this complicated method in the back end to solve for w and b.
6:25
But for most learning algorithms, including how you implement linear regression yourself, gradient descents are often a better way to get the job done.
6:35
In the optional lab that follows this video, you see how to define a multiple regression model in code, and also how to calculate the prediction f of x.
6:46
You also see how to calculate the cost and implement gradient descent for a multiple linear regression model.
6:54
This will be using Python's NumPy library, so if any of the code looks very new, that's okay.
7:01
But you should feel free also to take a look at the previous optional lab that introduces NumPy and vectorization for a refresher of NumPy functions and how to implement those in code.
7:14
So that's it. You now know multiple linear regression.
7:18
This is probably the single most widely used learning algorithm in the world today.
7:23
But there's more. With just a few tricks, such as picking and scaling features appropriately, and also choosing the learning rate alpha appropriately, you'll be able to make this work much better.
7:34
So just a few more videos to go for this week. Let's go on to the next video to see those little tricks that'll help you make multiple linear regression work much better.