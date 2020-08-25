# Web Notes

### robots.txt

**robots.txt**是一种存放于**网站根目录下**的ASCII编码的文本文件，它通常告诉网络搜索引擎的漫游器（又称**爬虫**），此网站中的哪些内容是**不应被搜索引擎的漫游器获取的**，哪些是**可以被漫游器获取**的。

这个协议也不是一个规范，而只是**约定俗成**的，有些搜索引擎会遵守这一规范，有些则不然。

### Google 用户代理令牌(User-agent)

| 抓取工具                                                     | 用户代理令牌（产品令牌）                                     | 完整的用户代理字符串                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **[APIs-Google](https://support.google.com/webmasters/answer/7426684)** | `APIs-Google`                                                | `APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)` |
| **[AdSense](https://support.google.com/adsense/answer/99376)** | `Mediapartners-Google`                                       | `Mediapartners-Google`                                       |
| [**AdsBot Mobile Web Android**](https://support.google.com/google-ads/answer/2404197)（检查 Android 网页广告质量） | `AdsBot-Google-Mobile`                                       | `Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)` |
| [**AdsBot Mobile Web**](https://support.google.com/google-ads/answer/2404197)（检查 iPhone 网页广告质量） | `AdsBot-Google-Mobile`                                       | `Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)` |
| **[AdsBot](https://support.google.com/google-ads/answer/2404197)**（检查桌面设备网页广告质量） | `AdsBot-Google`                                              | `AdsBot-Google (+http://www.google.com/adsbot.html`)         |
| **[Googlebot Image](https://support.google.com/webmasters/answer/35308)** | `Googlebot-Image``Googlebot`                                 | `Googlebot-Image/1.0`                                        |
| **[Googlebot News](https://support.google.com/news/publisher-center/answer/9606634)** | `Googlebot-News``Googlebot`                                  | `Googlebot-News`                                             |
| **Googlebot Video**                                          | `Googlebot-Video``Googlebot`                                 | `Googlebot-Video/1.0`                                        |
| **[Googlebot](https://support.google.com/webmasters/answer/182072)**（桌面版） | `Googlebot`                                                  | `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html`) `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z‡ Safari/537.36`  或（很少使用）：  `Googlebot/2.1 (+http://www.google.com/bot.html`) |
| **[Googlebot](https://support.google.com/webmasters/answer/182072)**（智能手机版） | `Googlebot`                                                  | `Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/*W.X.Y.Z*‡ Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)` |
| **[Mobile AdSense](https://support.google.com/adsense/answer/99376)** | `Mediapartners-Google`                                       | （各类移动设备）(`compatible; Mediapartners-Google/2.1`; `+http://www.google.com/bot.html`) |
| [**Mobile Apps Android**](https://support.google.com/google-ads/answer/2404197)（检查 Android 应用页面广告质量。遵守 AdsBot-Google 漫游器规则。） | `AdsBot-Google-Mobile-Apps`                                  | `AdsBot-Google-Mobile-Apps`                                  |
| **[Feedfetcher](https://support.google.com/webmasters/answer/178852)** | `FeedFetcher-Google`不遵循 robots.txt 规则 - [查看原因](https://support.google.com/webmasters/answer/178852#robots) | `FeedFetcher-Google; (+http://www.google.com/feedfetcher.html)` |
| **[Google Read Aloud](https://support.google.com/webmasters/answer/9274005)** | `Google-Read-Aloud`不遵循 robots.txt 规则 - [查看原因](https://support.google.com/webmasters/answer/9274005#robots) | 现用代理： `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36 (compatible; Google-Read-Aloud; +https://support.google.com/webmasters/answer/1061943)`曾用代理（已弃用）： `google-speakr` |
| **[Duplex on the Web](https://support.google.com/webmasters/answer/9467408)** | `DuplexWeb-Google`可能会忽略 * 用户代理通配符 - [查看原因](https://support.google.com/webmasters/answer/9467408#control-crawling) | `Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012; DuplexWeb-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36` |
| **Google Favicon**（检索各种服务的网站元素）                 | `Google Favicon`对于用户发起的请求，会忽略 robots.txt 规则   | `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon` |
| **[Web Light](https://support.google.com/webmasters/answer/6211428)** | `googleweblight`不遵循 robots.txt 规则 - [查看原因](https://support.google.com/webmasters/answer/6211428#robots) | `Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19` |