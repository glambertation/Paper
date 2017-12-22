* 判断
    * hasattr(resp, "BaseResp")
    * isinstance(content, basestring)

* unicode
    * isinstance(content, basestring) 非unicode
    * 转unicode
        * coding = 'utf-8'
        * content = content.decode(coding) 转unicode

* 内建函数
    * startswith 判断开头结尾
        * ``` if not self.content.startswith('<p>') or not self.content.endswith('</p>'): ```
        * ``` self.content = '<p>' + self.content + '</p>' #  <p></p>开头结尾 ```

* urlencode
     * 当url地址含有中文或者“/”的时候，这是就需要用做urlencode一下编码转换。
     * 解编码
        * urllib.unquote(content)

* beautifulsoup 正则

* repr
    * 这个函数，对应repr(object)这个功能。意思是当需要显示一个对象在屏幕上时，将这个对象的属性或者是方法整理成一个可以打印输出的格式
    * 这个功能与eval也可以对应。打印出的结果直接放到eval里，通常可以获得原来的对象
    * 比如：print repr(s) : ===> datetime.datetime(2014, 9, 9, 6, 34, 29, 756000)
