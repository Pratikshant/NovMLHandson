{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q1. Python factorial function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def facto(self):\n",
    "    self=int(self)\n",
    "    fact=1\n",
    "    for i in range(1,self+1):\n",
    "        fact = fact*i\n",
    "    return(fact)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "facto(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q2. Luke family relations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "skywalker={'Darth Vader':\"father\",'Leia':\"sister\",\"Han\":\"brother in law\",\"R2D2\":\"droid\"}\n",
    "def relation_to_luke(self):\n",
    "    print(\"Luke, I am your\", skywalker[self])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Luke, I am your droid\n"
     ]
    }
   ],
   "source": [
    "relation_to_luke(\"R2D2\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q3. Digits in a number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def NoDoNumber(self):\n",
    "    c=0\n",
    "    while (self>1):\n",
    "        self=self/10\n",
    "        c=c+1\n",
    "    return c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "NoDoNumber(725392)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q4. Multiplication of Factorials (Using facto function in Q1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def facto(self):\n",
    "    self=int(self)\n",
    "    fact=1\n",
    "    for i in range(1,self+1):\n",
    "        fact = fact*i\n",
    "    return(fact)\n",
    "def factomul(self):\n",
    "    self=int(self)\n",
    "    factmul=1\n",
    "    for i in range(1,self+1):\n",
    "        factmul = factmul*facto(i)\n",
    "    return(factmul)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "34560"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "factomul(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q5. Squared Sum of unknown numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def squaredsum(*ip):\n",
    "    sum=0\n",
    "    for i in ip:\n",
    "        sum=sum+(i*i)\n",
    "    return sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "38"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "squaredsum(2,0,5,3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q6. Arithmetic operations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def arithmetics (n1,n2,op):\n",
    "    if op=='+':\n",
    "        return n1+n2\n",
    "    elif op=='-':\n",
    "        return n1-n2\n",
    "    elif op=='*':\n",
    "        return n1*n2\n",
    "    elif op=='/':\n",
    "        return n1/n2\n",
    "    else:\n",
    "        print(\"this operation is not supported\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arithmetics (4,6,\"+\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q7. I Can I Will"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def canwill(n):\n",
    "    [d,r]=divmod(n,2)\n",
    "    if r==1:\n",
    "        print(\"I CAN\")\n",
    "    while (d>0):\n",
    "        print(\"I WILL\")\n",
    "        print(\"I CAN\")  \n",
    "        d=d-1       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I WILL\n",
      "I CAN\n",
      "I WILL\n",
      "I CAN\n",
      "I WILL\n",
      "I CAN\n",
      "I WILL\n",
      "I CAN\n"
     ]
    }
   ],
   "source": [
    "canwill(8)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q8. Number of Glove pairs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def numberofpairs(self):\n",
    "    p=0\n",
    "    import numpy as np\n",
    "    a1=np.array(self)\n",
    "    a1.sort()\n",
    "    i=0\n",
    "    while (i<len(a1)-1):\n",
    "        if a1[i]==a1[i+1]:\n",
    "            p=p+1\n",
    "            i=i+2\n",
    "        else:\n",
    "            i=i+1\n",
    "    return p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numberofpairs([1,2,1,2,1,2,3,3,4])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q9. Consecutive sequence"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "def consecutive_combo(l1,l2):\n",
    "    l3=l1+l2\n",
    "    l4=range(min(l3),max(l3)+1)\n",
    "    if len(l3)==len(l4):\n",
    "        return True\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "consecutive_combo([1,4,7,6],[5,3,2])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q10. Profit using dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "def profit(self):\n",
    "    dict= self\n",
    "    proft= (dict[\"sell_price\"]-dict[\"cost_price\"])*dict[\"inventory\"]\n",
    "    return int(round(1.0*proft))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3342"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "profit({\"cost_price\":11.5,\"sell_price\":15,\"inventory\":955})"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
