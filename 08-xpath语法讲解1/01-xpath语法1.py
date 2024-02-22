from lxml import etree

path = '''
    <body style="">
  
    

    
    



    <script type="text/javascript">var _body_start = new Date();</script><link href="//img3.doubanio.com/dae/accounts/resources/ded47ae/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <a href="https://accounts.douban.com/passport/login?source=movie" class="nav-login" rel="nofollow">登录/注册</a>
</div>


    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&amp;direct_dl=1&amp;download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&amp;direct_dl=1&amp;download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="">
      <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="on">
      <a href="https://movie.douban.com" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com/?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://fm.douban.com/?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com/?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com/?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">豆品</a>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/ded47ae/shire/bundle.js" defer="defer"></script>




    



    <link href="//img3.doubanio.com/dae/accounts/resources/ded47ae/movie/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-movie" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https://movie.douban.com">豆瓣电影</a>
    </div>
    <div class="nav-search">
      <form action="https://search.douban.com/movie/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="搜索电影、电视剧、综艺、影人" value="" autocomplete="off"></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1002">
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li><a href="https://movie.douban.com/cinema/nowplaying/">影讯&amp;购票</a>
    </li>
    <li><a href="https://movie.douban.com/explore">选电影</a>
    </li>
    <li><a href="https://movie.douban.com/tv/">电视剧</a>
    </li>
    <li><a href="https://movie.douban.com/chart">排行榜</a>
    </li>
    <li><a href="https://movie.douban.com/review/best/">影评</a>
    </li>
    <li><a href="https://movie.douban.com/annual/2023/?fullscreen=1&amp;source=navigation">2023年度榜单</a>
    </li>
    <li><a href="https://c9.douban.com/app/standbyme-2023/?autorotate=false&amp;fullscreen=true&amp;hidenav=true&amp;monitor_screenshot=true&amp;source=web_navigation" target="_blank">2023年度报告</a>
    </li>
  </ul>
</div>

    <a href="https://movie.douban.com/annual/2023/?fullscreen=1&amp;source=movie_navigation" class="movieannual"></a>
  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'movie_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= img}}" width="40" />
            <p>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                {{if sub_title}}
                    <br /><span>{{= sub_title}}</span>
                {{/if}}
                {{if address}}
                    <br /><span>{{= address}}</span>
                {{/if}}
                {{if episode}}
                    {{if episode=="unknow"}}
                        <br /><span>集数未知</span>
                    {{else}}
                        <br /><span>共{{= episode}}集</span>
                    {{/if}}
                {{/if}}
            </p>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/ded47ae/movie/bundle.js" defer="defer"></script>





    
    <div id="wrapper">
        

        
    <div id="content">
        
    <h1>豆瓣电影 Top 250</h1>

        <div class="grid-16-8 clearfix">
            
            
            <div class="article">
                







<div class="opt mod">
    <div class="tabs">
      
    

    </div>
    <span id="mine-selector">
      <input type="checkbox" value="unwatched">我没看过的
    </span>
</div>



<ol class="grid_view">
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">1</em>
                    <a href="https://movie.douban.com/subject/1292052/">
                        <img width="100" alt="肖申克的救赎" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292052/" class="">
                            <span class="title">肖申克的救赎</span>
                                    <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
                                <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
                            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.7</span>
                                <span property="v:best" content="10.0"></span>
                                <span>2988574人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">希望让人自由。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">2</em>
                    <a href="https://movie.douban.com/subject/1291546/">
                        <img width="100" alt="霸王别姬" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2561716440.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1291546/" class="">
                            <span class="title">霸王别姬</span>
                                <span class="other">&nbsp;/&nbsp;再见，我的妾  /  Farewell My Concubine</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 陈凯歌 Kaige Chen&nbsp;&nbsp;&nbsp;主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...<br>
                            1993&nbsp;/&nbsp;中国大陆 中国香港&nbsp;/&nbsp;剧情 爱情 同性
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.6</span>
                                <span property="v:best" content="10.0"></span>
                                <span>2208102人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">风华绝代。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">3</em>
                    <a href="https://movie.douban.com/subject/1292720/">
                        <img width="100" alt="阿甘正传" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2372307693.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292720/" class="">
                            <span class="title">阿甘正传</span>
                                    <span class="title">&nbsp;/&nbsp;Forrest Gump</span>
                                <span class="other">&nbsp;/&nbsp;福雷斯特·冈普</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 罗伯特·泽米吉斯 Robert Zemeckis&nbsp;&nbsp;&nbsp;主演: 汤姆·汉克斯 Tom Hanks / ...<br>
                            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 爱情
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.5</span>
                                <span property="v:best" content="10.0"></span>
                                <span>2226876人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">一部美国近现代史。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">4</em>
                    <a href="https://movie.douban.com/subject/1292722/">
                        <img width="100" alt="泰坦尼克号" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p457760035.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292722/" class="">
                            <span class="title">泰坦尼克号</span>
                                    <span class="title">&nbsp;/&nbsp;Titanic</span>
                                <span class="other">&nbsp;/&nbsp;铁达尼号(港 / 台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 詹姆斯·卡梅隆 James Cameron&nbsp;&nbsp;&nbsp;主演: 莱昂纳多·迪卡普里奥 Leonardo...<br>
                            1997&nbsp;/&nbsp;美国 墨西哥&nbsp;/&nbsp;剧情 爱情 灾难
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.5</span>
                                <span property="v:best" content="10.0"></span>
                                <span>2263974人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">失去的才是永恒的。 </span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">5</em>
                    <a href="https://movie.douban.com/subject/1295644/">
                        <img width="100" alt="这个杀手不太冷" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p511118051.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1295644/" class="">
                            <span class="title">这个杀手不太冷</span>
                                    <span class="title">&nbsp;/&nbsp;Léon</span>
                                <span class="other">&nbsp;/&nbsp;终极追杀令(台)  /  杀手莱昂</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 吕克·贝松 Luc Besson&nbsp;&nbsp;&nbsp;主演: 让·雷诺 Jean Reno / 娜塔莉·波特曼 ...<br>
                            1994&nbsp;/&nbsp;法国 美国&nbsp;/&nbsp;剧情 动作 犯罪
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.4</span>
                                <span property="v:best" content="10.0"></span>
                                <span>2358080人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">怪蜀黍和小萝莉不得不说的故事。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">6</em>
                    <a href="https://movie.douban.com/subject/1291561/">
                        <img width="100" alt="千与千寻" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2557573348.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1291561/" class="">
                            <span class="title">千与千寻</span>
                                    <span class="title">&nbsp;/&nbsp;千と千尋の神隠し</span>
                                <span class="other">&nbsp;/&nbsp;神隐少女(台)  /  千与千寻的神隐</span>
                        </a>


                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 宫崎骏 Hayao Miyazaki&nbsp;&nbsp;&nbsp;主演: 柊瑠美 Rumi Hîragi / 入野自由 Miy...<br>
                            2001&nbsp;/&nbsp;日本&nbsp;/&nbsp;剧情 动画 奇幻
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.4</span>
                                <span property="v:best" content="10.0"></span>
                                <span>2309970人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">最好的宫崎骏，最好的久石让。 </span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">7</em>
                    <a href="https://movie.douban.com/subject/1292063/">
                        <img width="100" alt="美丽人生" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2578474613.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292063/" class="">
                            <span class="title">美丽人生</span>
                                    <span class="title">&nbsp;/&nbsp;La vita è bella</span>
                                <span class="other">&nbsp;/&nbsp;一个快乐的传说(港)  /  Life Is Beautiful</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 罗伯托·贝尼尼 Roberto Benigni&nbsp;&nbsp;&nbsp;主演: 罗伯托·贝尼尼 Roberto Beni...<br>
                            1997&nbsp;/&nbsp;意大利&nbsp;/&nbsp;剧情 喜剧 爱情 战争
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.5</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1364065人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">最美的谎言。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">8</em>
                    <a href="https://movie.douban.com/subject/1889243/">
                        <img width="100" alt="星际穿越" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2614988097.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1889243/" class="">
                            <span class="title">星际穿越</span>
                                    <span class="title">&nbsp;/&nbsp;Interstellar</span>
                                <span class="other">&nbsp;/&nbsp;星际启示录(港)  /  星际效应(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 克里斯托弗·诺兰 Christopher Nolan&nbsp;&nbsp;&nbsp;主演: 马修·麦康纳 Matthew Mc...<br>
                            2014&nbsp;/&nbsp;美国 英国 加拿大&nbsp;/&nbsp;剧情 科幻 冒险
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.4</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1922876人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">爱是一种力量，让我们超越时空感知它的存在。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">9</em>
                    <a href="https://movie.douban.com/subject/3541415/">
                        <img width="100" alt="盗梦空间" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p513344864.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/3541415/" class="">
                            <span class="title">盗梦空间</span>
                                    <span class="title">&nbsp;/&nbsp;Inception</span>
                                <span class="other">&nbsp;/&nbsp;潜行凶间(港)  /  全面启动(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 克里斯托弗·诺兰 Christopher Nolan&nbsp;&nbsp;&nbsp;主演: 莱昂纳多·迪卡普里奥 Le...<br>
                            2010&nbsp;/&nbsp;美国 英国&nbsp;/&nbsp;剧情 科幻 悬疑 冒险
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.4</span>
                                <span property="v:best" content="10.0"></span>
                                <span>2130510人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">诺兰给了我们一场无法盗取的梦。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">10</em>
                    <a href="https://movie.douban.com/subject/1295124/">
                        <img width="100" alt="辛德勒的名单" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p492406163.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1295124/" class="">
                            <span class="title">辛德勒的名单</span>
                                    <span class="title">&nbsp;/&nbsp;Schindler's List</span>
                                <span class="other">&nbsp;/&nbsp;舒特拉的名单(港)  /  辛德勒名单</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 史蒂文·斯皮尔伯格 Steven Spielberg&nbsp;&nbsp;&nbsp;主演: 连姆·尼森 Liam Neeson...<br>
                            1993&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 历史 战争
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.5</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1152408人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">拯救一个人，就是拯救整个世界。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">11</em>
                    <a href="https://movie.douban.com/subject/1292064/">
                        <img width="100" alt="楚门的世界" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p479682972.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292064/" class="">
                            <span class="title">楚门的世界</span>
                                    <span class="title">&nbsp;/&nbsp;The Truman Show</span>
                                <span class="other">&nbsp;/&nbsp;真人Show(港)  /  真人戏</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 彼得·威尔 Peter Weir&nbsp;&nbsp;&nbsp;主演: 金·凯瑞 Jim Carrey / 劳拉·琳妮 Lau...<br>
                            1998&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 科幻
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.4</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1781600人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">如果再也不能见到你，祝你早安，午安，晚安。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">12</em>
                    <a href="https://movie.douban.com/subject/3011091/">
                        <img width="100" alt="忠犬八公的故事" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2587099240.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/3011091/" class="">
                            <span class="title">忠犬八公的故事</span>
                                    <span class="title">&nbsp;/&nbsp;Hachi: A Dog's Tale</span>
                                <span class="other">&nbsp;/&nbsp;秋田犬八千(港)  /  忠犬小八(台)</span>
                        </a>


                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 莱塞·霍尔斯道姆 Lasse Hallström&nbsp;&nbsp;&nbsp;主演: 理查·基尔 Richard Ger...<br>
                            2009&nbsp;/&nbsp;美国 英国&nbsp;/&nbsp;剧情
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.4</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1432779人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">永远都不能忘记你所爱的人。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">13</em>
                    <a href="https://movie.douban.com/subject/1292001/">
                        <img width="100" alt="海上钢琴师" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2574551676.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292001/" class="">
                            <span class="title">海上钢琴师</span>
                                    <span class="title">&nbsp;/&nbsp;La leggenda del pianista sull'oceano</span>
                                <span class="other">&nbsp;/&nbsp;声光伴我飞(港)  /  一九零零的传奇</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 朱塞佩·托纳多雷 Giuseppe Tornatore&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗斯 Tim Roth / ...<br>
                            1998&nbsp;/&nbsp;意大利&nbsp;/&nbsp;剧情 音乐
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.3</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1724457人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">每个人都要走一条自己坚定了的路，就算是粉身碎骨。 </span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">14</em>
                    <a href="https://movie.douban.com/subject/3793023/">
                        <img width="100" alt="三傻大闹宝莱坞" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p579729551.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/3793023/" class="">
                            <span class="title">三傻大闹宝莱坞</span>
                                    <span class="title">&nbsp;/&nbsp;3 Idiots</span>
                                <span class="other">&nbsp;/&nbsp;三个傻瓜(台)  /  作死不离3兄弟(港)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 拉库马·希拉尼 Rajkumar Hirani&nbsp;&nbsp;&nbsp;主演: 阿米尔·汗 Aamir Khan / 卡...<br>
                            2009&nbsp;/&nbsp;印度&nbsp;/&nbsp;剧情 喜剧 爱情 歌舞
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.2</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1911457人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">英俊版憨豆，高情商版谢耳朵。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">15</em>
                    <a href="https://movie.douban.com/subject/1291549/">
                        <img width="100" alt="放牛班的春天" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2884280708.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1291549/" class="">
                            <span class="title">放牛班的春天</span>
                                    <span class="title">&nbsp;/&nbsp;Les choristes</span>
                                <span class="other">&nbsp;/&nbsp;歌声伴我心(港)  /  唱诗班男孩</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 克里斯托夫·巴拉蒂 Christophe Barratier&nbsp;&nbsp;&nbsp;主演: 让-巴蒂斯特·莫尼...<br>
                            2004&nbsp;/&nbsp;法国 瑞士 德国&nbsp;/&nbsp;剧情 音乐
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.3</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1352644人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">天籁一般的童声，是最接近上帝的存在。 </span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">16</em>
                    <a href="https://movie.douban.com/subject/2131459/">
                        <img width="100" alt="机器人总动员" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1461851991.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/2131459/" class="">
                            <span class="title">机器人总动员</span>
                                    <span class="title">&nbsp;/&nbsp;WALL·E</span>
                                <span class="other">&nbsp;/&nbsp;太空奇兵·威E(港)  /  瓦力(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 安德鲁·斯坦顿 Andrew Stanton&nbsp;&nbsp;&nbsp;主演: 本·贝尔特 Ben Burtt / 艾丽...<br>
                            2008&nbsp;/&nbsp;美国&nbsp;/&nbsp;科幻 动画 冒险
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.3</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1356365人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">小瓦力，大人生。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">17</em>
                    <a href="https://movie.douban.com/subject/25662329/">
                        <img width="100" alt="疯狂动物城" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2614500649.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/25662329/" class="">
                            <span class="title">疯狂动物城</span>
                                    <span class="title">&nbsp;/&nbsp;Zootopia</span>
                                <span class="other">&nbsp;/&nbsp;优兽大都会(港)  /  动物方城市(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 拜伦·霍华德 Byron Howard / 瑞奇·摩尔 Rich Moore&nbsp;&nbsp;&nbsp;主演: 金妮弗·...<br>
                            2016&nbsp;/&nbsp;美国&nbsp;/&nbsp;喜剧 动画 冒险
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.2</span>
                                <span property="v:best" content="10.0"></span>
                                <span>2016303人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">迪士尼给我们营造的乌托邦就是这样，永远善良勇敢，永远出乎意料。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">18</em>
                    <a href="https://movie.douban.com/subject/1307914/">
                        <img width="100" alt="无间道" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2564556863.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1307914/" class="">
                            <span class="title">无间道</span>
                                    <span class="title">&nbsp;/&nbsp;無間道</span>
                                <span class="other">&nbsp;/&nbsp;Infernal Affairs  /  Mou gaan dou</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 刘伟强 / 麦兆辉&nbsp;&nbsp;&nbsp;主演: 刘德华 Andy Lau / 梁朝伟 Tony Leung Chiu W...<br>
                            2002&nbsp;/&nbsp;中国香港&nbsp;/&nbsp;剧情 犯罪 惊悚
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.3</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1412858人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">香港电影史上永不过时的杰作。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">19</em>
                    <a href="https://movie.douban.com/subject/1296141/">
                        <img width="100" alt="控方证人" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1505392928.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1296141/" class="">
                            <span class="title">控方证人</span>
                                    <span class="title">&nbsp;/&nbsp;Witness for the Prosecution</span>
                                <span class="other">&nbsp;/&nbsp;雄才伟略  /  情妇</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 比利·怀尔德 Billy Wilder&nbsp;&nbsp;&nbsp;主演: 泰隆·鲍华 Tyrone Power / 玛琳·...<br>
                            1957&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 犯罪 悬疑
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.6</span>
                                <span property="v:best" content="10.0"></span>
                                <span>597995人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">比利·怀德满分作品。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">20</em>
                    <a href="https://movie.douban.com/subject/1292213/">
                        <img width="100" alt="大话西游之大圣娶亲" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2455050536.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292213/" class="">
                            <span class="title">大话西游之大圣娶亲</span>
                                    <span class="title">&nbsp;/&nbsp;西遊記大結局之仙履奇緣</span>
                                <span class="other">&nbsp;/&nbsp;西游记完结篇仙履奇缘  /  齐天大圣西游记</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 刘镇伟 Jeffrey Lau&nbsp;&nbsp;&nbsp;主演: 周星驰 Stephen Chow / 吴孟达 Man Tat Ng...<br>
                            1995&nbsp;/&nbsp;中国香港 中国大陆&nbsp;/&nbsp;喜剧 爱情 奇幻 古装
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.2</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1576462人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">一生所爱。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">21</em>
                    <a href="https://movie.douban.com/subject/5912992/">
                        <img width="100" alt="熔炉" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1363250216.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/5912992/" class="">
                            <span class="title">熔炉</span>
                                    <span class="title">&nbsp;/&nbsp;도가니</span>
                                <span class="other">&nbsp;/&nbsp;无声呐喊(港)  /  漩涡</span>
                        </a>


                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 黄东赫 Dong-hyuk Hwang&nbsp;&nbsp;&nbsp;主演: 孔侑 Yoo Gong / 郑有美 Yu-mi Jung /...<br>
                            2011&nbsp;/&nbsp;韩国&nbsp;/&nbsp;剧情
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.4</span>
                                <span property="v:best" content="10.0"></span>
                                <span>958430人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">我们一路奋战不是为了改变世界，而是为了不让世界改变我们。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">22</em>
                    <a href="https://movie.douban.com/subject/1291841/">
                        <img width="100" alt="教父" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p616779645.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1291841/" class="">
                            <span class="title">教父</span>
                                    <span class="title">&nbsp;/&nbsp;The Godfather</span>
                                <span class="other">&nbsp;/&nbsp;Mario Puzo's The Godfather</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 弗朗西斯·福特·科波拉 Francis Ford Coppola&nbsp;&nbsp;&nbsp;主演: 马龙·白兰度 M...<br>
                            1972&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 犯罪
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.3</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1001069人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">千万不要记恨你的对手，这样会让你失去理智。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">23</em>
                    <a href="https://movie.douban.com/subject/6786002/">
                        <img width="100" alt="触不可及" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1454261925.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/6786002/" class="">
                            <span class="title">触不可及</span>
                                    <span class="title">&nbsp;/&nbsp;Intouchables</span>
                                <span class="other">&nbsp;/&nbsp;闪亮人生(港)  /  逆转人生(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 奥利维·那卡什 Olivier Nakache / 艾力克·托兰达 Eric Toledano&nbsp;&nbsp;&nbsp;主...<br>
                            2011&nbsp;/&nbsp;法国&nbsp;/&nbsp;剧情 喜剧
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.3</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1160344人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">满满温情的高雅喜剧。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">24</em>
                    <a href="https://movie.douban.com/subject/1849031/">
                        <img width="100" alt="当幸福来敲门" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2614359276.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1849031/" class="">
                            <span class="title">当幸福来敲门</span>
                                    <span class="title">&nbsp;/&nbsp;The Pursuit of Happyness</span>
                                <span class="other">&nbsp;/&nbsp;寻找快乐的故事(港)  /  追求快乐</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 加布里尔·穆奇诺 Gabriele Muccino&nbsp;&nbsp;&nbsp;主演: 威尔·史密斯 Will Smith ...<br>
                            2006&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 传记 家庭
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.2</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1562337人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">平民励志片。 </span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">25</em>
                    <a href="https://movie.douban.com/subject/20495023/">
                        <img width="100" alt="寻梦环游记" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2505426431.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/20495023/" class="">
                            <span class="title">寻梦环游记</span>
                                    <span class="title">&nbsp;/&nbsp;Coco</span>
                                <span class="other">&nbsp;/&nbsp;玩转极乐园(港)  /  可可夜总会(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 李·昂克里奇 Lee Unkrich / 阿德里安·莫利纳 Adrian Molina&nbsp;&nbsp;&nbsp;主演: ...<br>
                            2017&nbsp;/&nbsp;美国&nbsp;/&nbsp;喜剧 动画 奇幻 音乐
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.1</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1750719人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">死亡不是真的逝去，遗忘才是永恒的消亡。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
</ol>



    
    
    

        <div class="paginator">
        <span class="prev">
            &lt;前页
        </span>
        
        

                <span class="thispage">1</span>
                
            <a href="?start=25&amp;filter=">2</a>
        
                
            <a href="?start=50&amp;filter=">3</a>
        
                
            <a href="?start=75&amp;filter=">4</a>
        
                
            <a href="?start=100&amp;filter=">5</a>
        
                
            <a href="?start=125&amp;filter=">6</a>
        
                
            <a href="?start=150&amp;filter=">7</a>
        
                
            <a href="?start=175&amp;filter=">8</a>
        
                
            <a href="?start=200&amp;filter=">9</a>
        
                
            <a href="?start=225&amp;filter=">10</a>
        
        <span class="next">
            <link rel="next" href="?start=25&amp;filter=">
            <a href="?start=25&amp;filter=">后页&gt;</a>
        </span>

            <span class="count">(共250条)</span>
        </div>



            </div>
            <div class="aside">
                
<p class="pl">
    豆瓣用户每天都在对“看过”的电影进行“很差”到“力荐”的评价，豆瓣根据每部影片看过的人数以及该影片所得的评价等综合数据，通过算法分析产生豆瓣电影 Top 250。
</p>

<div id="dale_movie_top250_bottom_right" ad-status="loaded" data-sell-type="RTB" data-type="YoudaoRender" data-version="3.2.41"></div>

<!-- douban ad begin -->




<link rel="stylesheet" href="https://img1.doubanio.com/f/movie/400d7765546ceac9b07913937f6a29d532d41690/dist/movie/ad/mobile_app_ad.css">
<div class="mobile-app-entrance block5 app-movie">
    <a class="entrance-link" href="https://www.douban.com/doubanapp/frodo">
        <div class="entrance-qrcode">
            <img src="https://img1.doubanio.com/f/movie/a02f6ed325fc52e220f299d51e730c422e2bcd16/pics/movie/douban_app_ad/qrcode.png" alt="扫码下载豆瓣 App" width="80" height="80">
        </div>
        <div class="entrance-info">
            <span class="app-icon icon-movie"></span>
            <span class="main-title">豆瓣</span>
            <span class="sub-title">让好电影来找你</span>
        </div>
    </a>
</div>

<!-- douban ad end -->


            </div>
            <div class="extra">
                
            </div>
        </div>
    </div>

        
    <div id="footer">
            <div class="footer-extra"></div>
        
<span id="icp" class="fleft gray-link">
    © 2005－2024 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about/legal">法律声明</a>
    
    · <a href="https://help.douban.com/?app=movie" target="_blank">帮助中心</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

    </div>

    </div>
    <!-- COLLECTED JS -->
        
        
    <link rel="stylesheet" type="text/css" href="https://img1.doubanio.com/f/vendors/0035bb2f83e2cba49ecf634fed57f9ff1bbd0d09/css/ui/dialog.css">
    <link rel="stylesheet" type="text/css" href="https://img1.doubanio.com/f/movie/9dbc931479d6c183e970ea3594672460b6c96b3c/dist/movie/mod/login_pop.css">
    <script type="text/javascript" src="https://img1.doubanio.com/f/vendors/f25ae221544f39046484a823776f3aa01769ee10/js/ui/dialog.js"></script>
    <script type="text/javascript">
        var HTTPS_DB = "https://www.douban.com"
    </script>
    <script type="text/javascript" src="https://img1.doubanio.com/f/movie/c9e1b0aba08d78a747e52b55cd7dfe54fc4e5d8f/dist/movie/mod/login_pop.js"></script>

    
    




    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '',
            browserId = '2EDMAFrpBAw',
            criteria = '3:/top250',
            preview = '',
            debug = false,
            adSlots = ['dale_movie_top250_bottom_right'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', '//img1.doubanio.com/bG90MDZqMy9mL2FkanMvYzhmZjE5MGNhYzNkN2UyMWJjMTI3NzJlYWNkOWVkODZhMmFjMzdhMi9hZC5yZWxlYXNlLmpz?company_token=kX69T8w1wyOE-dale');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>







    <script type="text/javascript">
        $(function(){
            $("#mine-selector input[type='checkbox']").click(function(){
                var val = $(this).is(":checked")?$(this).val():"";
                window.location.href = '/top250?filter=' + val;
            })
        })
    </script>

    
  









<script type="text/javascript">
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript';
    g.defer=true;
    g.async=true;
    g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-19', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id]);
      _gaq.push([method('_setSampleRate'), '5']);

      
  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '0', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
}


;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>








      

    <!-- dae-web-movie--default-8b9bd587d-9zvnl-->

  <script>_SPLITTEST=''</script>





<div id="search_suggest" style="display: none; top: 78px; left: 163.906px;"><ul></ul></div></body>
'''

# 实例化一个etree对象
tree = etree.HTML(path)

# 获取span标签
# span = tree.xpath('//span')
# print(span,len(span))

# # 获取img标签
# img = tree.xpath('//img')
# print(img)

# 获取span标签
# span1 = tree.xpath('//p/span')
# print(span1)
# for i in span1:
#     print(i.text)

# 获取span标签的文本内容
# span2 = tree.xpath('//p/span/text()')
# print(span2)

# 获取img标签中的src值 使用@
# img = tree.xpath('//img/@src')
# print(img)

# 通过属性进行定位
# span = tree.xpath('//span[@class="title"]/text()')
# print(span)
# print(''.join(span))
# for i in span[1::2]:
#     print(''.join(i))
#     print('\n')

# 获取评分
# score = tree.xpath('//span[@class="rating_num"]/text()')
# print(score)

# 根据位置进行定位 xpath定位从1开始
title = tree.xpath('//div[@class="hd"]/a/span[1]/text()')
print(title)
