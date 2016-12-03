## Example

![example](http://i.imgur.com/DV5izE9.jpg)

```
python juxtapose.py 1.jpg 2.jpg
```

# juxtapose-py
Python script that given 2 images as input put them next to each other, or put the two half together. Useful to compare difference in edited images

### Prerequisites

This script make uses of the Python Imaging Library: PIL. You need to install it before running it

### Usage

You can use it by launching it like

```
python juxtapose.py <pathpics1> <pathpics2> [mode(optional)]
```

You can have a look at the parameter with 

```
python juxtapose.py -h
```

```
-m Mode to use:

Mode 0: Juxtapose the two half        <- Default
Mode 1: Put them next to each other
```

### Other Exemple 


```
python juxtapose.py 1.jpg 2.jpg -m 1
```

![example](http://i.imgur.com/6oihfGo.jpg)



### Final notes

If you were wondering how to achive the effect of the parrot image you might wanna check [letter-pics](https://github.com/powahftw/letters-pics)

This script was created to quickly compare the [letter-pics](https://github.com/powahftw/letters-pics) output and was made "to work". There might some small problem in error handling or better optimization possibile. I appreciate any type of feedback :) 
