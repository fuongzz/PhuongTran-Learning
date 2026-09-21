0:03
So far, we've just been fitting straight lines to our data.
0:06
Let's take the ideas of multiple linear regression and feature engineering to come up with a new algorithm called polynomial regression,
0:14
which lets you fit curves, nonlinear functions, to your data.
0:18
Let's say you have a housing dataset that looks like this, where feature x is the size in square feet.
0:25
It doesn't look like a straight line fits this dataset very well.
0:29
So maybe you want to fit a curve, maybe a quadratic function, to the data, like this, which includes a size, x, and also x squared,
0:40
which is the size raised to the power of 2.
0:43
And maybe that will give you a better fit to the data.
0:47
But then you may decide that your quadratic model doesn't really make sense,
0:50
because the quadratic function eventually comes back down.
0:54
And, well, we wouldn't really expect housing prices to go down when the size increases, right?
0:59
Big houses seem like they should usually cost more.
1:03
So then you may choose a cubic function, where we now have not only x squared, but x cubed.
1:11
So maybe this model produces this curve here, which is a somewhat better fit to the data,
1:17
because the size does eventually come back up as the size increases.
1:22
These are both examples of polynomial regression,
1:25
because you took your optional feature x and raised it to the power of 2 or 3 or any other power.
1:33
And in the case of the cubic function, the first feature is the size,
1:37
the second feature is the size squared, and the third feature is the size cubed.
1:43
I just want to point out one more thing,
1:46
which is that if you create features that are these powers,
1:49
like the square of the original features like this,
1:52
then feature scaling becomes increasingly important.
1:56
So if the size of the house ranges from, say, 1 to 1,000 square feet,
2:01
then the second feature, which is the size squared, would range from 1 to a million,
2:07
and the third feature, which is size cubed, ranges from 1 to a billion.
2:13
So these two features, x squared and x cubed,
2:17
take on very different ranges of values compared to the optional feature x.
2:22
And if you're using gradient descent,
2:24
it's important to apply feature scaling to get your features into comparable ranges of values.
2:31
Finally, here's one last example of how you really have a wide range of choices of features to use.
2:38
Another reasonable alternative to taking the size squared and size cubed is to, say, use the square root of x.
2:45
So your model may look like w1 times x plus w2 times the square root of x plus b.
2:54
The square root function looks like this, and it becomes a bit less steep as x increases,
3:00
but it doesn't ever completely flatten out, and it certainly never, ever comes back down.
3:06
So this would be another choice of features that might work well for this data set as well.
3:11
So you may ask yourself, how do I decide what features to use?
3:16
Later in the second course in this specialization,
3:19
you see how you can choose different features and different models that include or don't include these features,
3:25
and you have a process for measuring how well these different models perform
3:30
to help you decide which features to include or not include.
3:34
For now, I just want you to be aware that you have a choice in what features you use,
3:39
and by using feature engineering and polynomial functions,
3:42
you can potentially get a much better model for your data.
3:47
In the optional lab that follows this video,
3:50
you will see some code that implements polynomial regression using features like x, x squared, and x cubed.
3:57
So please take a look and run the code and see how it works.
4:02
There's also another optional lab after that one that shows how to use a popular open-source toolkit
4:08
that implements linear regression.
4:12
Scikit-learn is a very widely used open-source machine learning library
4:17
that is used by many practitioners in many of the top AI, Internet, machine learning companies in the world.
4:25
So if either now or in the future you're using machine learning in your job,
4:30
there's a very good chance you'll be using tools like Scikit-learn to train your models.
4:36
And so working through that optional lab will give you a chance to not only better understand linear regression,
4:42
but also see how this can be done in just a few lines of code using a library like Scikit-learn.
4:49
For you to have a solid understanding of these algorithms and be able to apply them,
4:55
I do think it's important that you know how to implement linear regression yourself
4:59
and not just call some Scikit-learn function that is a black box.
5:03
But Scikit-learn also has an important role in the way machine learning is done in practice today.
5:09
So we're just about at the end of this week.
5:13
Congratulations on finishing all of this week's videos.
5:16
Please do take a look at the practice quizzes and also the practice lab,
5:21
which I hope will let you try out and practice ideas that we've discussed.
5:26
In this week's practice lab, you implement linear regression.
5:30
I hope you have a lot of fun getting this learning algorithm to work for yourself.
5:34
Best of luck with that.
5:36
And I also look forward to seeing you in next week's videos,
5:40
where we'll go beyond regression, that is predicting numbers,
5:43
to talk about our first classification algorithm, which can predict categories.
5:48
I'll see you next week.