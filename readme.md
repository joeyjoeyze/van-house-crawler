# Van House Crawler

## Description

The scripts fetch house renting posts in Vancouver from other websites and write the information to MongoDB.

## How to use

```bash
$ python fetch
```

## VanPeople

<details>

<summary>Example information that can get from <a href="http://www.vanpeople.com/c/list/1.html">VanPeople</a></summary>

```json
{
    "images": ["http://www.vanpeople.com/c/uploadpic/<image-date>/<image-id>.jpg"],
    "link": "http://www.vanpeople.com/c/<post-id>.html",
    "description": "<description>",
    "title": "<title>",
    "date": "<year>/<month>/<day> <hour>:<minute>:<second>",
    "details": {
        "qq": "<qq>",
        "area": "<area>",
        "price": "$<price>|面议",
        "telephone": "<area-code>-<3-digits-phone-number>-<4-digits-phone-number>",
        "contact": "<name>",
        "wechat": "<wechat>",
        "address": "<address>"
    }
}
```

Note: `link`, `description`, `title`, `date`, `details.area`, `details.price`, `details.telephone` are guaranteed 
non-empty values

</details>
