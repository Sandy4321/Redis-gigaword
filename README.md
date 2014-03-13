Redis-gigaword
==============

Redis code used to do TrueCasing  using a 5-gram Language Model . Language Model generated using Gigaword corpus.

Truecasing is the process of restoring case for a sentence. For instance, a sentence in English, say, __"it is SUNny outside in vancouver"__ will be restored to, __"It is sunny outside in Vancouver"__. 

If you are thinking, will "VaNcOUvER" change to "Vancouver", you bet it will! 

**So, what is the point of this project ?**

Well, truecasing is one of the many tasks in Natural language processing that uses a language model. A language model, in simple terms, is just a gigantic hash table. But, the aim of this project was to see if distributing this gigantic table among various instances balanced out the load and made the process faster, end-to-end. How did we find that? 

Well, we used Redis. 

**Why use Redis ?**

Multiple reasons really. To learn about Redis. Redis is a key:value data store, which fits perfectly with storing something like a language model. Also, Redis provides two things we wanted, namely, persistence and high availability. Persistence implies that we load the language model once, and after that, even if the system crashes, the data is written to disk  in the RDB format and can be loaded back in a jiffy. Also, we had an expectation that despite a couple hundred concurrent clients, there would be no alarming latency in the process. And finally, it is unfair on Redis to call it just a key:value data store. It provides a host of other data structures to be used, like, sets, sorted lists, lists and hashes ! 


How to use the scripts 
======================

I cannot release the data as its released only via LDC. But, we can use a word count file from http://norvig.com/ngrams/count_big.txt . A snapshot of the file looks like : 

a	21160
aah	1
aaron	5
ab	2
aback	3
abacus	1
abandon	32

Word followed by its count. In a language model, it would be different that the counts would be replaced by _backoff_ values. Say, you want to write this file to redis. You can use the script 

<pre>
python WritingCorpus.py filename
</pre>

There are more details, with more analysis, and results, in http://bit.ly/10WI73s 



 


 

Thank you.  
