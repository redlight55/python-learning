1. What is []?
It is an empty list. A list that contains no values.

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

`spam[2] = 'hello'`


For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

3. What does spam[int(int('3' * 2) // 11)] evaluate to?

`['d']`

4. What does spam[-1] evaluate to?

`['d']`

5. What does spam[:2] evaluate to?
`['a', 'b']`


For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to?
1

7. What does bacon.append(99) make the list value in bacon look like?
`[3.14, 'cat', 11, 'cat', True, 99]`

8. What does bacon.remove('cat') make the list value in bacon look like?
`[3.14, 11, 'cat', True]`

9. What are the operators for list concatenation and list replication?
To combine two lists to create a new list, use '+'. To replicate a list that is usually used with an integer value, use '*'.

Example
`spam = ['cat', 'bat', 'rat']`
`cheese = ['moose', 'goose']`

List concatenation
`spam_and_cheese = spam + cheese`
`spam_and_cheese is now ['cat', 'bat', 'rat', 'moose', 'goose']`

List replication
`spam_is_spam = spam * 3`
spam is now `['cat', 'bat', 'rat', 'cat', 'bat', 'rat', 'cat', 'bat', 'rat']`

10. What is the difference between the append() and insert() list methods?
`append()` adds the argument at the end of the list while `insert()` allows the value to be added at any index in the list. `insert()` takes two arguments, the first is the index of the new value, the second is the new value to be inserted.

11. What are two ways to remove values from a list?
The first is using the `remove()` method which is simply `list_name.remove(value_here)`.
The second is using the `del` method where it is best if you know the index of the value you want to delete.

12. Name a few ways that list values are similar to string values.

13. What is the difference between lists and tuples?
First is the how it is typed. Tuples are typed with parentheses while lists are typed with square brackets.
Second is that unlike lists, tuples are immutable ie. they cannot have their values modified, appended, or removed.
Third is to indicate a tuple, one places a comma at near the value at the end. This lets Python know the intended assignment is a type tuple.

14. How do you type the tuple value that has just the integer value 42 in it?
`((42,))`

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
By converting the list into a tuple like so
`tuple([list])`

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
They contain references to a list, not the list value itself. If one refers the list in another variable, any changes to the new variable will affect the original.

17. What is the difference between copy.copy() and copy.deepcopy()?
`copy.copy()` will copy the list and allows the original to be maintained if any changes are made to the new copy. `copy.deepcopy()` allows for lists inside a list to be copied and allows it to be changed while maintaining the values of the original.