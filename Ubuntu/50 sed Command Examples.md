# 50 `sed` Command Examples

[toc]

`sed` is a useful text processing feature of GNU/Linux. The full form of `sed` is Stream Editor. Many types of simple and complicated text processing tasks can be done very easily by using `sed` command. Any particular string in a text or a file can be searched, replaced and deleted by using regular expression with `sed` command. But this commands performs all types of modification temporarily and the original file content is not changed by default. The user can store the modified content into another file if needs. The basic uses of `sed` command are explained in this tutorial by using 50 unique examples. Before starting this tutorial you must check the installed version of `sed` in your operating system by running the following command. The tutorial is designed based on GNU sed. So this version of `sed` will be required to practice the examples shown in this tutorial.

```bash
sed --version
```

<img src="50%20sed%20Command%20Examples.assets/image-20220905165606923.png" alt="image-20220905165606923" style="zoom:50%;" />

The following output shows that GNU Sed of version 4.4 is installed in the system.

## 1. Basic text substitution

```bash
echo "Bash Scripting Language" | sed 's/Bash/Perl/'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220905170232574.png" alt="image-20220905170232574" style="zoom:50%;" />

Create a text file named **`weekday.txt`** with the following content.

```
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
```

```bash
cat weekday.txt
sed 's/Sunday/Sunday is holiday/' weekday.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220905222240267.png" alt="image-20220905222240267" style="zoom: 50%;" />

## 2. Replace all instances of a text in a particular line of a file using `g` option

`g` option is used to replace all occurrences of matching pattern. Create a text file named **`python.txt`** with the following content. This file contains the word '**Python**' multiple times.

```
Python is a very popular language.
Python is easy to use. Python is easy to learn.
Python is a cross-platform language
```

```bash
cat python.txt
sed '2 s/Python/Perl/g' python.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220905223047527.png" alt="image-20220905223047527" style="zoom:50%;" />

## 3. Replace the second occurrence only of a match on each line

```bash
cat python.txt
sed 's/Python/Perl/g2' python.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220905224510215.png" alt="image-20220905224510215" style="zoom:50%;" />

## 4. Replace the last occurrence only of a match on each line

Create a text file named **`lang.txt`** with the following content.

```
Bash Programming Language.  Python Programming Language. Perl Programming Language.
Hypertext Markup Language.
Extensible Markup Language.
```

The regular expression `.*` matches texts follows the greedy strategy. `\1` represents the matched text that contained in the parentheses `\( \)`.

```bash
cat lang.txt
sed 's/\(.*\)Programming/\1Scripting/' lang.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220905224736788.png" alt="image-20220905224736788" style="zoom:50%;" />

## 5. Replace the first match in a file with new text

```bash
cat python.txt
sed '1 s/Python/Perl/' python.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906093551883.png" alt="image-20220906093551883" style="zoom:50%;" />

## 6. Replace the last match in a file with new text

`$` symbol is used to match the last occurrence of the pattern.

```bash
cat python.txt
sed -e '$ s/Python/Bash/' python.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906093756547.png" alt="image-20220906093756547" style="zoom:50%;" />

## 7. Escaping backslash in replace commands to manage search and replace of file paths

It is necessary to escape the backslash in the file path for searching and replacing. The following command will add backslash `\` in the file path.

```bash
echo /home/ubuntu/code/perl/add.pl | sed 's;/;\\/;g'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906094342129.png" alt="image-20220906094342129" style="zoom:50%;" />

## 8. Replace all files full path with just the filename no directory

The filename can be retrieved from the file path very easily by using `basename` command. `sed` command can also be used to retrieve the filename from the file path.

```bash
echo "/home/ubuntu/temp/myfile.txt" | sed 's/.*\///'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906094530438.png" alt="image-20220906094530438" style="zoom:50%;" />

## 9. Substitute text but only if some other text is found in the string

Create a file named **`dept.txt`** with the following content to replace any text based on other text.

```
List of Total Students:

CSE - Count
EEE - Count
Civil - Count
```

```bash
cat dept.txt
sed  -e '/CSE/ s/Count/100/; /EEE/ s/Count/70/;' dept.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906094636944.png" alt="image-20220906094636944" style="zoom:50%;" />

## 10. Substitute text but only if some other text is not found in the string

```bash
cat dept.txt
sed -i -e '/CSE/! s/Count/80/;' dept.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906094821011.png" alt="image-20220906094821011" style="zoom:50%;" />

## 11. Add string before and after the matching pattern using `\1`

The sequence of matching patterns of `sed` command is denoted by `\1`, `\2` and so on. The following command will search the pattern, '**Bash**' and if the pattern matches then it will be accessed by `\1` in the part of replacing text.

```bash
echo "Bash language" | sed  's/\(Bash\)/Learn \1 programming/'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906095816442.png" alt="image-20220906095816442" style="zoom:50%;" />

## 12. Delete matching lines

`d` option is used to delete any line from the file. Create a file named **`os.txt`** with the following content.

```
Windows
Linux
Android
OS
```

The following command will delete those lines that contains the text, '**OS**'.

```bash
cat os.txt
sed '/OS/d' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906100203899.png" alt="image-20220906100203899" style="zoom:50%;" />

## 13. Delete matching line and 2 lines after matching line

```bash
sed '/Linux/,+2d' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906100439440.png" alt="image-20220906100439440" style="zoom:50%;" />

## 14. Delete all spaces at end of the line of text

`[:blank:]` class can be used to remove spaces and tabs from the text or the content of any file. The following command will remove the spaces at the end of each line. 

```bash
cat os.txt
sed 's/[[:blank:]]*$//' os.txt
```

## 15. Delete all lines that have a match two times on the line

Create a text file named **`input.txt`** with the following content and delete those lines of the file that contains the searching pattern two times.

```
PHP is a server-side scripting language.
PHP is an open-source language and PHP is case-sensitive.
PHP is platform-independent.
```

'**PHP**' text contains two times in the second line. Two sed commands are used in this example to remove those lines that contain the pattern '**php**' two times. The first sed command will replace the second occurrence of '**php**' in each line by '**dl**' and send the output into the second sed command as input. The second sed command will delete those lines that contain the text, '**dl**'.

```bash
cat input.txt
sed 's/php/dl/i2;t' input.txt | sed '/dl/d'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906101833553.png" alt="image-20220906101833553" style="zoom:50%;" />

## 16. Delete all lines that have only white-space

`^$` is used to find out the empty lines in the file.

```bash
cat input.txt
sed '/^$/d' input.txt
```

## 17. Delete all non-printable characters

Non-printable characters can be deleted from any text by replacing non-printable characters by none. `[:print:]` class is used in this example to find out the non-printable characters. `\t` is a non-printable character and it can’t be parsed directly by the `echo` command. For this, `\t` character is assigned in a variable, $tab that is used in an `echo` command. The output of the `echo` command is sent in the `sed` command that will remove the character `\t` from the output.

```bash
tab=$'\t'
echo Hello"$tab"World
echo Hello"$tab"World | sed 's/[^[:print:]]//g'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906103658060.png" alt="image-20220906103658060" style="zoom:50%;" />

## 18. If there is a match in line append something to end of line

```bash
cat os.txt
sed '/Windows/ s/$/ 10/' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906131724929.png" alt="image-20220906131724929" style="zoom:50%;" />

## 19. If there is a match in the line insert a line before the text

```bash
cat input.txt
sed '/PHP is platform-independent/ s/^/PHP is an interpreted language.\n/' input.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906131917113.png" alt="image-20220906131917113" style="zoom:50%;" />

## 20. If there is a match in the line insert a line after that line

```bash
cat os.txt
sed 's/Linux/&\nUbuntu/' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906132314208.png" alt="image-20220906132314208" style="zoom:50%;" />

## 21. If there is not a match append something to the end of line

```bash
cat os.txt
sed '/Linux/! s/$/ Operating System/' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906132539313.png" alt="image-20220906132539313" style="zoom:50%;" />

## 22. If there is not a match delete the line

Create a file named **`web.txt`** with the following content

```
HTML 5
JavaScript
CSS
PHP
MySQL
JQuery
```

The following command will search and delete those lines that do not contain the text, '**CSS**'.

```bash
cat web.txt
sed '/CSS/! d' web.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906133357086.png" alt="image-20220906133357086" style="zoom:50%;" />

## 23. Duplicate matched text after adding a space after the text

```bash
cat python.txt
sed -e 's/to /& to/g' python.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906133704166.png" alt="image-20220906133704166" style="zoom:50%;" />

## 24. Replace one list of strings with the new string

**`list1.txt`**

```
1001 => Jafar Ali
1023 => Nir Hossain
1067 => John Michel
```

**`list2.txt`**

```
1001    CSE     GPA-3.63
1002    CSE     GPA-3.24
1023    CSE     GPA-3.11
1067    CSE     GPA-3.84
```

match the first column of the two text files shown above and replace the matching text with the value of the third column of the file **`list1.txt`**

```bash
cat list1.txt
cat list2.txt
sed `cat list1.txt | awk '{print "-e s/"$1"/"$3"/"}'`<<<"`cat list2.txt`"
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906163242178.png" alt="image-20220906163242178" style="zoom:50%;" />

## 25. Replace the matched string with a string that contains newlines

```bash
echo "Bash Perl Python Java PHP ASP" | sed 's/Python/Added Text\n/'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906164502224.png" alt="image-20220906164502224" style="zoom:50%;" />

## 26. Remove newlines from file and insert a comma at end of each line

`-z` option is used to separate the line by NULL character.

```bash
sed -z 's/\n/,/g' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906164737176.png" alt="image-20220906164737176" style="zoom:50%;" />

## 27. Remove commas and add newline to split the text into multiple lines

```bash
echo "Kaniz Fatema,30th,batch" | sed "s/,/\n/g"
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906165407951.png" alt="image-20220906165407951" style="zoom:50%;" />

## 28. Find case insensitive match and delete line

`I` is used for the case-insensitive match that indicates ignore case.

```bash
cat os.txt
sed '/linux/Id' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220906165609017.png" alt="image-20220906165609017" style="zoom:50%;" />

## 29. Find case insensitive match and replace with new text

```bash
echo "I like bash programming " | sed 's/Bash/PHP/i'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907110259588.png" alt="image-20220907110259588" style="zoom:50%;" />

## 30. Find case insensitive match and replace with all uppercase of the same text

`\U` is used to convert any text to all uppercase letter.

```bash
cat os.txt
sed 's/\(linux\)/\U\1/Ig' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907110550850.png" alt="image-20220907110550850" style="zoom:50%;" />

## 31. Find case insensitive match and replace with all lowercase of same text

`\L` is used to convert any text to all lowercase letters.

```bash
cat os.txt
sed 's/\(linux\)/\L\1/Ig' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907111556734.png" alt="image-20220907111556734" style="zoom:50%;" />

## 32. Replace all uppercase characters of the text with lowercase characters

```bash
cat os.txt
$ sed  's/\(.*\)/\L\1/' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907121944379.png" alt="image-20220907121944379" style="zoom:50%;" />

## **33. Search for number in line and append any currency symbol before the** number

**`items.txt`**

```
HDD       100
Monitor   80
Mouse     10
```

```bash
cat items.txt
sed 's/\([0-9].*\)/$\1/g' items.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907122646293.png" alt="image-20220907122646293" style="zoom:50%;" />

## 34. Add commas to numbers that have more than 3 digits

`:a` indicates the label and `ta` is used to iterate grouping process.

```bash
echo "5098673" | sed -e :a -e 's/\(.*[0-9]\)\([0-9]\{3\}\)/\1,\2/;ta'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907123925733.png" alt="image-20220907123925733" style="zoom:50%;" />

## 35. Replaces tab character with 4 space characters

`$` symbol is used to match the tab character and `g` is used to replace all tab characters.

```bash
echo -e "1\t2\t3" | sed $'s/\t/    /g'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907124236499.png" alt="image-20220907124236499" style="zoom:50%;" />

## 36. Replaces 4 consecutive space characters with tab character

```bash
echo -e "1    2" | sed $'s/    /\t/g'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907124329443.png" alt="image-20220907124329443" style="zoom:50%;" />

## 37. Truncate all lines to first 80 characters

**`in.txt`**

```
PHP is a server-side scripting language.
PHP is an open-source language and PHP is case-sensitive. PHP is faster. PHP is platform-independent.
```

```bash
cat in.txt
sed 's/\(^.\{1,80\}\).*/\1/' in.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907124717205.png" alt="image-20220907124717205" style="zoom:50%;" />

## 38. Search for a string regex and append some standard text after it

```bash
echo "hello, how are you?" | sed 's/\(hello\)/\1 John/'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907130511670.png" alt="image-20220907130511670" style="zoom:50%;" />

## 39. Search for string regex and append some text after the second match in each line

```bash
cat input.txt
sed 's/\(PHP\)/\1 (New Text added)/2' input.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907130258873.png" alt="image-20220907130258873" style="zoom:50%;" />

## 40. Running multi-line sed scripts from a file

`-f` option is used to execute `sed` script from the file.

**`sedcmd`**

```
s/PHP/ASP/
s/independent/dependent/
```

```bash
cat sedcmd
sed -f sedcmd input.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907131213915.png" alt="image-20220907131213915" style="zoom:50%;" />

## 41. Match a multi-line pattern and replace with new multi-line text

`P` and `D` are used for multi-line processing.

```bash
cat os.txt
sed '$!N;s/Linux\nAndroid/Ubuntu\nAndoid Lollipop/;P;D' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907140426042.png" alt="image-20220907140426042" style="zoom:50%;" />

## 42. Replace order of two words in a text that match a pattern

```bash
echo "perl python" | sed -e 's/\([^ ]*\) * \([^ ]*\)/\2 \1/'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907133332511.png" alt="image-20220907133332511" style="zoom:50%;" />

## 43. Execute multiple sed commands from the command-line

```bash
echo "Ubuntu Centos Debian" | sed -e 's/Ubuntu/Kubuntu/; s/Centos/Fedora/'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907133556798.png" alt="image-20220907133556798" style="zoom:50%;" />

## 44. Combine sed with other commands

```bash
cat os.txt | sed 's/Linux/Fedora/'| sed 's/windows/Windows 10/i'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907133647120.png" alt="image-20220907133647120" style="zoom:50%;" />

## 45. Insert empty line in a file

**`stdlist`**

```
#ID     #Name
[101]   -Ali
[102]   -Neha
```

`G` option is used to insert empty line in a file.

```bash
cat stdlist
sed G stdlist
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907133828252.png" alt="image-20220907133828252" style="zoom:50%;" />

## 46. Replace all alpha-numeric characters by space in each line of a file.

```bash
cat stdlist
sed 's/[A-Za-z0-9]/ /g' stdlist
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907133941712.png" alt="image-20220907133941712" style="zoom:50%;" />

## 47. Use `&` to print matched string

`p` is used to print the modified text.

```bash
sed -n 's/^L/Matched String is - &/p' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907134105854.png" alt="image-20220907134105854" style="zoom:50%;" />

## 48. Switch pair of words in a file

**`course.txt`**

```
PHP            ASP
MySQL          Oracle
CodeIgniter    Laravel
```

```bash
cat course.txt
sed  's/\([^ ]*\) *\([^ ]*\)/\2 \1/' course.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907134342457.png" alt="image-20220907134342457" style="zoom:50%;" />

## 49. Capitalize the first character of each word

```bash
echo "I like bash programming" | sed 's/\([a-z]\)\([a-zA-Z0-9]*\)/\u\1\2/g'
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907134426983.png" alt="image-20220907134426983" style="zoom:50%;" />

## 50. Print line numbers of the file

`=` symbol is used to print the line number before each line of a file.

```bash
sed '=' os.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907134748425.png" alt="image-20220907134748425" style="zoom:50%;" />

## 51. Replace Newline With Space

```bash
cat test.txt
sed -e ':a;N;$!ba;s/\n/ /g' test.txt
```

- `:a:` Creates a label ‘a’
- `N`: Appends the next line to the pattern space
- `$!ba`: If not the last line, returns to label ‘a’
- `s/\n/ /g`: Finds and replaces newline (`\n`) with space (`/ /`). The pattern is matched globally (`/g`)

```bash
sed -z -e 's/\n/ /g' test.txt
tr '\n' ' ' < test.txt
perl -p -e 's/\n/ /' test.txt
paste -s -d ' ' test.txt
awk 1 ORS=' ' test.txt
```

<img src="50%20sed%20Command%20Examples.assets/image-20220907141947644.png" alt="image-20220907141947644" style="zoom:50%;" />
