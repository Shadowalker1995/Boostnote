# 可以在JSON文件中使用注释吗

JSON 文件中没有真正的注释，文件中全是数据。如果你写入注释，那这也是数据。

你可以自定义一个元素例如 _comment, 在你的应用中忽视 _comment 数据。

有时候注释是很有用的，如下

```json
{
   "_comment": "here is comment",
   "glossary": {
      "title": "example glossary",
      "GlossDiv": {
         "title": "S",
         "GlossList": {
            "GlossEntry": {
               "ID": "SGML",
               "SortAs": "SGML",
               "GlossTerm": "Standard Generalized Markup Language",
               "Acronym": "SGML",
               "Abbrev": "ISO 8879:1986",
               "GlossDef": {
                  "para": "A meta-markup language, used to create markup languages such as DocBook.",
                  "GlossSeeAlso": ["GML", "XML"]
               },
               "GlossSee": "markup"
            }
         }
      }
   }
}
```

### Reference

http://blog.topspeedsnail.com/page/148