# Unofficial 1CAK API
Unofficial 1cak API build using Flask

## Single Post

```
http://localhost:5000/get-post/{id}
```

### Parameter
| Parameter        | Description                                                                     |
|------------------|-------------------------------------------------------------------------------|
| **id** _required_ | post id (int) |

### Example

GET ```http://localhost:5000/get-post/2979366```

**Response** 

```
{   
    "id":2979366,
    "image":"https://1cak.com/posts/49acff2dea769748e93eb5a0a6c64eb7_t.jpg",
    "link":"https://1cak.com/2979366",
    "nsfw":false,
    "title":"Jaman dimana safety masih di nomor 69420"
}
```
## Categorized Post

```
http://localhost:5000/get-categorized/{category}/{hours_ago}
```

### Parameter
| Parameter        | Description                                                                     |
|------------------|-------------------------------------------------------------------------------|
| **category** _required_ | category (str), expected input: {lol, trending, recent, legendary} |
| **hours_ago** _required_ | n hours ago (int) |

### Example

GET ```http://localhost:5000/get-categorized/lol/15```

**Response** 

```
{
    "category":"lol",
    "posts":[
        {
            "id":"2979369",
            "image":"https://1cak.com/posts/68f31fcf154ead0a3c946afabcc82aca_t.jpg",
            "link":"https://1cak.com/2979369",
            "nsfw":false,
            "title":"Niat mau BAB malah nolongin temen"
        },
        {
            "id":"2979367",
            "image":"https://1cak.com/posts/44312cb1ec1e013d23c41c26fe94c9f7_t.jpg",
            "link":"https://1cak.com/2979367",
            "nsfw":false,
            "title":"Karena Nyari Duit Lebih Penting"
        },
        {
            "id":"2979366",
            "image":"https://1cak.com/posts/49acff2dea769748e93eb5a0a6c64eb7_t.jpg",
            "link":"https://1cak.com/2979366",
            "nsfw":false,
            "title":"Jaman dimana safety masih di nomor 69420"
        }
    ]
}
```

## Random Post (Shuffle)

```
http://api-1cak.herokuapp.com/random
```

**Response** 

```
{
    "id":"2037577",
    "image":"https://cdn16.1cak.com/posts/154cd259aefefc7c1835cde3117750c8_t.jpg",   
    "link":"https://1cak.com/2037577",
    nsfw":false,
    "title":"Bawa binatang peliharaan di malaysia vs Russia"
}
```
