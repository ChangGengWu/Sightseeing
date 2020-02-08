-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 2019 年 12 月 11 日 08:26
-- 伺服器版本： 10.4.8-MariaDB
-- PHP 版本： 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `homestead`
--

-- --------------------------------------------------------

--
-- 資料表結構 `user_comment`
--

CREATE TABLE `user_comment` (
  `id` int(10) NOT NULL,
  `name` varchar(120) NOT NULL,
  `href` varchar(180) NOT NULL,
  `comment` varchar(1500) NOT NULL,
  `site_ID` varchar(150) DEFAULT NULL,
  `site` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `user_comment`
--

INSERT INTO `user_comment` (`id`, `name`, `href`, `comment`, `site_ID`, `site`) VALUES
(3766, '程 舜', 'https://www.tripadvisor.com.tw/Profile/Connector810984', '「2019福隆國際沙雕藝術季」活動時間持續到8月25日止，今年以「穿越小鎮尋找亞特蘭提斯」為主題，結合觀光局「2019小鎮漫遊年」與「亞特蘭提斯」海洋議題，規劃出「與神同行」、「穿越古今」、「海洋之美」三大展區，邀請7國(臺灣、日本、韓國、新加坡、馬來西亞、中國、加拿大)25位沙雕藝術家齊力在福隆沙灘創作出精彩的沙雕作品。 有幸圍觀了6/15所舉辦的金氏世界紀錄海豚沙雕創舉! 300座海豚齊聚福隆沙灘的盛況十分震撼!!太精采了!!', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3767, '愛七桃', 'https://www.tripadvisor.com.tw/Profile/Compass809761', '福隆國際沙雕藝術是每年必來的，福隆的砂質好，被評選為台灣最適合沙雕的場所， 每年沙雕藝術季都會邀請世界各地沙雕師傅，精緻的沙雕藝術作品，回程可再去吃個福隆便當，會是不錯的選擇', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3768, 'Ming C', 'https://www.tripadvisor.com.tw/Profile/MingC622', '很特別的一個活動，親身體驗到原來沙雕也可以是一門藝術，絕對不是小朋友玩泥沙～！現場很多沙雕都充滿創意，目不暇給～！', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3769, '程 舜', 'https://www.tripadvisor.com.tw/Profile/Connector810984', '「2018福隆國際沙雕藝術季」運用創新思維融入互動體驗，從六縣十島、「顛倒」主雕、精彩的國內外競賽沙雕，到夜間沙雕秀、地下沙雕，加上親民的百人沙雕創作，不斷推陳出新，受到民眾喜愛，沙雕季帶給旅客有感體驗，讓東北角成為友好的觀光好事！', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3770, 'ACE', 'https://www.tripadvisor.com.tw/Profile/nonstopthinking', '這幾年的夏日海灘加沙雕，辦得非常好，大型的國際沙雕，加上本地特色的沙雕，搭配起來真的很棒，只是每到假日都會很多人，停車一位難求，坐火車到福隆走過去五分鐘，會是好選擇！', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3771, '江南有丹橘', 'https://www.tripadvisor.com.tw/Profile/SteppingOrange', '每年五月到七月前後，是貢寮的國際沙雕藝術季的盛會，不管是來游泳的、來玩水的、來欣賞藝術作品的，絡繹不絕的遊客，把貢寮的海灘推向國際化。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3772, 'ShinRongWang', 'https://www.tripadvisor.com.tw/Profile/ShinRongWang', '夏天很適合全家一起來遊玩的地方，自己開車或是搭火車公車都可以到達，附近飲食也非常方便。 有很多家有名的便當店，可以一邊看海一邊吃午餐，如果沒有太熱感覺還不錯。 而且每年沙雕的主題都不同，所以每天都可以看到不同的沙雕。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3773, 'Meowmeow1211', 'https://www.tripadvisor.com.tw/Profile/Meowmeow1211', '因為這是一個七月的周末，在沙灘上同時舉行兩個夏季節日，可以想像會有很多人吧。如果正計劃去福隆參加慶祝活動，請確保早點上火車或巴士，人很多呢!', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3774, 'BL2047', 'https://www.tripadvisor.com.tw/Profile/BL2047', '台灣除了有很不錯的自然觀光資源外, 還有一些活動也很適合一家大小參與的, 包括這個  在夏季5-7月舉辦的福隆國際沙雕藝術季. 每年都吸引國內外好手共同參與，創作精彩的沙雕沙雕作品。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3775, 'Brilly L', 'https://www.tripadvisor.com.tw/Profile/BrillyLin', '這裡是沙雕迷的年度盛事。時常會邀請國內外知名藝術家來創作作品。每年的主題都有點不一樣。很適合一家大小都來逛逛', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3776, 'Hakuna W', 'https://www.tripadvisor.com.tw/Profile/HakunaW', '每年的國際沙雕展都像百花爭艷一樣，值得一看。從臺北市搭火車很快就到了福隆，跟著人潮走就可以看到沙雕展。適合帶小朋友一起來看，結束後再買個火車便當一飽口福！', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3777, 'Wang R', 'https://www.tripadvisor.com.tw/Profile/444wangr', '這幾年福隆沙雕已闖出了名號，非常推薦帶小孩子來欣賞，今年是12星座沙雕展，水準很高，乘坐台灣好行巴士即可抵達，但班次少，搭火車也可以到。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3778, 'C.Y.C.', 'https://www.tripadvisor.com.tw/Profile/yenchutw', '位於福隆沙灘上的造景，許多圖案極富巧思，讓人驚嘆藝術家的功力如此強大。若是帶兒童前來，還可順道讓孩子玩水～', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3779, 'ASA L', 'https://www.tripadvisor.com.tw/Profile/973asal', '有很大的沙雕，也有小的沙雕，有人物的，有動物的，有景物的。沙雕師高超精湛的工藝技術，打造出一座座很美的雕像。要尊重雕像哦，他們也是有生命，有靈魂的，不要惡意破壞哦。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3780, 'ViewRight', 'https://www.tripadvisor.com.tw/Profile/ViewRight', '每年夏初的福隆沙雕節, 是戲水外可以更增添樂趣的活動. 已經舉辦了許多年, 由於良好的大眾運輸更促進了這個活動的人潮. 很佩服這樣的沙雕可以長時間的活動中維護的良好, 沒有一次令人失望的', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3781, 'faifai18', 'https://www.tripadvisor.com.tw/Profile/faifai18', '我們家的小孩非常喜歡玩水，所以今年夏天我們到了台北的時候去了福隆玩水，小孩子帶了不少工具，在沙灘上造了不同的沙雕，我們趕快幫他拍了不少照，非常的好玩。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3782, 'Billbill08', 'https://www.tripadvisor.com.tw/Profile/Billbill08', '夏天來到福隆游水，記得參觀沙雕展。不同國家的選手齊集福隆沙灘，同沙砌出不同造型的沙雕，場面震撼。看過沙雕再去游水、玩獨木舟也不遲。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3783, 'Celia L', 'https://www.tripadvisor.com.tw/Profile/CeliaL922', '每年活動都會和附近商家異業合作，若不趕時間亦可以於活動前或期間購買相關套票；如此一來不僅可以觀賞國際級的沙雕藝術還可以同時遊覽附近的名勝，適合大人小孩攜家帶眷的活動，但要注意防曬及適時補充水分。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3784, '拉拉 摳', 'https://www.tripadvisor.com.tw/Profile/Sunshine669335', '福隆國際沙雕藝術季為推展臺灣的沙雕活動，建立國內沙雕藝術創作空間，讓臺灣的沙雕藝術能夠逐漸萌芽與發展，逐年締造一波波佳評如潮的踴躍佳績，每年都吸引國內外好手共同參與，創作沙雕作品。快來福隆國際沙雕藝術季，感受臺灣的活力熱情！', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3785, 'chung w', 'https://www.tripadvisor.com.tw/Profile/chungw117', '剛好這次來台北出差配合上福隆國際沙雕藝術季的活動，利用假日和朋友一同搭車前往，第一次看到這麼盛大的沙雕藝術，人很多但也很開心，對喜歡沙雕藝術的人一定會很愛這裡～', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3786, 'kxwsy', 'https://www.tripadvisor.com.tw/Profile/kxwsy', '說到陽光與海灘，一定少不了在沙灘上堆沙。沙雕藝術季正正提供了一個平台給有藝術天分的人們，可以運用自己的創意打造屬於自己的理想世界，看著小弟弟在努力的建築屬於自己的城堡，好像就看著小時候自己的夢想一樣。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3787, 'Sandy L', 'https://www.tripadvisor.com.tw/Profile/SandyL2845', '這個活動每年5月至7月在福隆海水浴場舉行，可欣賞到不少大師級的作品，令人嘆為觀止，是拍照的好地方。附近也可進行玩水、帆船、獨木舟等水上運動。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3788, 'stvleecw', 'https://www.tripadvisor.com.tw/Profile/stvleecw', '福隆參觀國際沙雕藝術季於五月至七月舉行，沙雕藝術在現場觀看只能用“非常厲害”來形容, 是非常獨特又富創作的藝術作品, 十分佩服！', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3789, 'fantasr', 'https://www.tripadvisor.com.tw/Profile/fantasr', '每年沙雕季總是吸引人關注，五月的太陽不算太大，但仍然會把你曬傷，除了到海邊玩水之餘，還能欣賞沙雕藝術。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3790, 'PETER', 'https://www.tripadvisor.com.tw/Profile/Maps810461', '這次我第一次來福隆國際沙雕藝術季，果然如傳說中的人多熱鬧，沙雕藝術真的很特別，感覺到作者都很用心做出自己最滿意的作品，這裡的交通也很方便，便當也很好吃，又可以玩水，真的是很值得推薦的好景點～', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3791, '洪萍萍', 'https://www.tripadvisor.com.tw/Profile/a691117', '走在沙灘裡看到ㄧ座座沙堆出來的模型，栩栩如生！讚嘆藝術家的巧手！照片殺不停生怕有漏網之魚！不過太陽真的好毒辣阿⋯⋯', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3792, 'Kin Chung L', 'https://www.tripadvisor.com.tw/Profile/KinChungL4', '福隆是台北人最喜歡去的海邊之一 就算沒有這個活動 還是會常常去福隆海水浴場 但這次剛好撞到沙雕節 想不到小時候的玩泥沙變得這麼壯觀', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3793, 'Futehsu', 'https://www.tripadvisor.com.tw/Profile/Futehsu', '交通很方便, 福隆海水浴場門票100元, 有沙雕展時一樣是100元很划算, 會請多國沙雕師來創作與比賽, 作品很大, 適合一群朋友來拍照. 需要注意夏天很曬, 建議帶傘及補充水分', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3794, '小明達人', 'https://www.tripadvisor.com.tw/Profile/BoardingPass809545', '在福隆舉辦的沙雕藝術季，真的好值得一家大細去，活動是免費的，又可以去沙灘玩玩水，去野餐，又有沙雕藝術品欣賞，真係一流。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3795, 'yuhan701123', 'https://www.tripadvisor.com.tw/Profile/yuhan701123', '前往福隆的交通 如果是搭火車會人很多 要有心理準備  沙灘上很熱沒有什麼遮蔽物 所以要做好防曬跟補充水份  沙雕很厲害很有創意 還可以在沙灘玩水 小孩很開心', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3796, 'viviennechui', 'https://www.tripadvisor.com.tw/Profile/viviennechui', '相信每個去過沙灘嘅人都去砌過城堡、河流，去到現場一看不得不讚嘆藝術者們的手藝高超，只用沙加水就可以堆砌出比人還要高的精彩展品', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3797, '490meiyic', 'https://www.tripadvisor.com.tw/Profile/490meiyic', '每年都會帶著小孩回去看沙雕，每一年都辦得很用心，我們全家會住在旁邊的芙蓉飯店，兩天一夜的時間剛剛好，家裡有小孩也很適合，從飯店旁邊的小路就可以直接走到沙灘上，小朋友玩水吃飯都很方便', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3798, 'AN03956', 'https://www.tripadvisor.com.tw/Profile/AN03956', '福隆沙雕展已經成為年度的夏天活動，很多國家的團隊都會來參與，可以看到非常多特別又具有創意的作品，非常推薦來看。可以順便搭配北海岸或東北角一帶的景點，做為一個充實的一日遊活動。不過海灘太陽非常曬，一定要做好防曬否則會被曬傷。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3799, 'shoywu', 'https://www.tripadvisor.com.tw/Profile/shoywu', '福隆國際沙雕藝術季是每年必看的精彩展覽，各家好手總能以單純的沙子塑出形形色色的有趣作品，是來到福隆旅遊時一定不可錯過的精彩活動。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3800, 'juniorForTA', 'https://www.tripadvisor.com.tw/Profile/juniorForTA', '如果本來就要來沙灘或海邊，沙雕就是免費觀賞的。近幾年都會有，可以在玩水或是沙灘排球之餘來看一下這些有趣的雕象，請不要破壞他們。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3801, 'CHIKA C', 'https://www.tripadvisor.com.tw/Profile/CHIKAC101', '福隆除了是夏天戲水的好所在，也是沙雕展出的重鎮。 由於台鐵交通方便，每到戲水時分總是湧入大量人潮，再搭配沙雕展更是人山人海；沙雕主題各年不同，像是12星座沙雕展，維妙維肖的刻劃出各星座的特色之處，相當合適拍照打卡。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3802, 'tangs0078', 'https://www.tripadvisor.com.tw/Profile/tangs0078', '福隆是許多台灣北部人夏日會前往的戲水聖地，尤其是在過去，許多少年及青少年的暑假都會在福隆海水浴場渡過，隨著出國遊外的風氣盛行，福隆已不再那麼受到歡迎，沙雕是後來興起的熱門活動，很適合親子同遊，讓下一代體驗一下台灣海洋的美好', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3803, 'Morrix', 'https://www.tripadvisor.com.tw/Profile/Morrix', '這個海水浴場是需要購買門票才可進入的，可是沙灘上四處還是可見許多的垃圾，管理單位是否要加強清潔才能讓遊客安心地玩樂！！', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3804, '118yuwenc', 'https://www.tripadvisor.com.tw/Profile/118yuwenc', '福隆沙雕藝術季每年都仍然有不少新創意，同時可看點也非常豐富！只是交通實在不夠方便，先不說開車一位難求，要坐火車到福隆更是人擠人...如果想前往參觀特色沙雕，一定要計畫好交通接駁...', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3805, '雪芳 林', 'https://www.tripadvisor.com.tw/Profile/W5390YV_', '建議坐火車過去比較不容易塞車，蠻多各式沙雕可以欣賞，配合週邊腳踏車道及玩水，一整天不累，肚子餓了可買火車站旁的福隆便當吃。', 'S0099', ' 福隆國際沙雕藝術季 Fulong International Sand Sculpture Festival'),
(3806, 'bpolar', 'https://www.tripadvisor.com.tw/Profile/bpolar', '袖珍博物館票價不貴，當初是在Gomaji上面買到優惠票，可以消磨個兩、三個小時。館藏豐富，每個展品都值得細細品味，往往會有令人驚喜的設計佈置，其用心可見一斑。另外還有一個小小的童玩區，大朋友可以回味童年，小朋友可以體驗父母小時候的樂趣。紀念品店販售很多製作袖珍模型的零件，有興趣的人可以好好逛逛。是個絕對值得一遊的小型博物館。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3807, '李克達', 'https://www.tripadvisor.com.tw/Profile/dake900', '地方沒有很大，但是作品很多而且都很精緻 地處於距離捷運較遠，所以好像知道的人沒有很多 很值得細細品嘗各國風景', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3808, 'theprolixbloc', 'https://www.tripadvisor.com.tw/Profile/theprolixbloc', '如果你在台北的時候碰上下雨天，這裏將會是一個很棒的駐足之地。如果你的時間很緊張，不建議你來這裏，但是如果你將在台北待很長一段時間，這裡有一些優秀的藝術作品。不是所有的作品都很棒，但是牆上那些出自布魯克·塔克和雷·惠特利奇之手的作品一定要看！一定要看看那些照片！', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3809, 'Friendychan 2018😋✈️🏨', 'https://www.tripadvisor.com.tw/Profile/friendychan', '好友喜歡看袖珍模型，我們就相約到此參觀  各式各樣的展品，如蛋殼雕花、在鴨蛋或鵝蛋內另闢一室的雕功，猶如鬼斧神工，真令人讚嘆不已！  還有各種袖珍的模型、場景、商店、大屋的不同房間⋯，都弄得栩栩如生，美極，妙極！', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3810, 'Nathan Mamico', 'https://www.tripadvisor.com.tw/Profile/nathanmamico', '這裡很不錯、、東西不算很多不過可以來大開眼界。逛不到一個小時、就逛完了。交通很方便、捷運、公車都能到', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3811, 'Carol', 'https://www.tripadvisor.com.tw/Profile/CarolChen1227', '地方不是很大，但是作品算滿多的。作品都很細膩，滿有趣的，值得去看看。滿有趣的～ 而且很漂亮～ 好像沒什麼人知道這地方，所以人很少。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3812, 'rain498', 'https://www.tripadvisor.com.tw/Profile/rain498', '無意中發現了這個地方，所以我們想為什麼不進來看看呢。博物館在一座辦公樓的地下室里。門票每人180元。我們在那裡呆了一個半小時。白金漢宮的模型是十二分之一的比例。我喜歡那些歐洲風格的房子模型，比如廚房、客廳，甚至兒童房。還有裁縫店、麵包店等。有些是根據格列佛遊記、匹諾曹等故事改編的。那裡有一家禮品店，如果你的話，可以在那裡買到紀念品。洗手間在博物館外面，但是不用擔心，因為工作人員會在你手上蓋標記，你可以在同一天內返回這裏。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3813, 'Miaw', 'https://www.tripadvisor.com.tw/Profile/JiaYunM', '參觀迷你世界，讓人神遊在不同情境。 如果帶小朋友參觀的話可以試著讓他們看圖說故事，會是很不錯的體驗喔。 ', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3814, 'jifu5867', 'https://www.tripadvisor.com.tw/Profile/jifu5867', '想去袖珍博物館很久了，周末剛好沒計畫，所以就安排了這次行程．袖珍博物館位於大樓地下室，所以不是很好找，所幸在路上有看到招牌．從一樓進去就可以看到指示．接著可以看到一道往地下室的入口，小小的樓梯，感覺要到甚麼神祕的地方．買完票，推開這道大門，就可以進去袖珍的世界，有點踏入不知領域的興奮感．  一進去可以看到是許多的娃娃玩偶，牆上還貼著娃娃屋的發展史．可以看到兩邊展示著各國不同工藝的娃娃，有些實在太逼真，加上最近安娜貝爾等鬼娃娃的電影太多，真的會越看越毛，所以沒有待很久就往下看． …', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3815, 'Elsa L', 'https://www.tripadvisor.com.tw/Profile/729elsal', '在地圖臨時搜尋附近境點, 由興安街步行十来分鐘就找到。 位處ㄧ商厦地牢, 地方不大, 展品可不少。入塲费NT180+20(護照)。展品都很精細, 認真到把相片都縮细至不及半隻指甲大。不經不覺就參觀了ㄧ個多小時。 適合喜歡精緻手作品的人士參觀。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3816, 'FreeSpirit', 'https://www.tripadvisor.com.tw/Profile/WaywardSoul999', '有趣的博物館，如果你喜歡微縮模型，那這是你必須参觀的地方。我們沒想到會在這個博物館待2個小時，因為我們認為能在30-40分鐘內参觀完畢。這裡有超多可看的東西，你也可以在他們的紀念品商店買一些微型紀念品。有些東西並不便宜，但那真的取決於你有多喜歡微型模型。最後但同樣重要的是，紀念品商店內有咖啡櫃檯，你可以在那裡買到飲料或冰淇淋。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3817, 'neta a', 'https://www.tripadvisor.com.tw/Profile/780netaa', '其實我們來到這裏並沒有很高的期望，但是事實上卻吃了一驚，非常棒的展覽，我非常喜歡，真的應該再多花些時間嘗試去了解更多的小細節，強烈推薦！非常喜歡他們的商店，給自己買了很多袖珍模型！！！', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3818, 'Leonhkny', 'https://www.tripadvisor.com.tw/Profile/Leonhkny', '這個小型私人博物館位於一座商業大樓的地下室。從松江南京地鐵站步行走一小段路，它展示了大量的迷你房屋。英國皇家閱兵式的場景是我們最喜歡的。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3819, '台灣俏妞世界趴趴走', 'https://www.tripadvisor.com.tw/Profile/graceczozo', '小時候最喜歡的博物館之一， 記得在電視上看到後~就跟媽媽吵著一定要去! 地方雖然不大~但真的很讓人驚艷! 而且每個東西都有他的特色~還有那個很小的電視~ 真的有東西播放!真的很酷!!', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3820, '392pandac', 'https://www.tripadvisor.com.tw/Profile/392pandac', '在商業大樓的地下室，地方不大，但展品精細，有些是作者花上五年精心製作的傑作，有些則是二百年前的作品！', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3821, 't86841283', 'https://www.tripadvisor.com.tw/Profile/t86841283', '博物館在一棟大樓的地下一樓，入口不是很顯眼，但裡面展品絕對讓大人小孩都目不轉睛。入館前館員會問是從哪來的，據說是要統計來客的區域分佈，很有趣。附設賣店也有賣很多袖珍物品。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3822, '江南有丹橘', 'https://www.tripadvisor.com.tw/Profile/SteppingOrange', '靠近馬路旁的一間奇妙的博物館，加上他在建國高架橋旁邊，若開車來，可以找到停車位的旅客，或許可以順道過來看看。  不過他需要收費，所以比較少觀光客入內，若沒仔細看招牌，會以為他是促銷的賣場。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3823, 'ChaioI', 'https://www.tripadvisor.com.tw/Profile/ChaioI', '地點在大樓的地下室，裡面有很多有趣的收藏，很適合全家大小遊玩的地方。但門票有點小貴，館內空間也不是很寬敞，但仍值得走訪一趟。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3824, 'Lucky Travel Junkie', 'https://www.tripadvisor.com.tw/Profile/LuckyTravelJunkie', '當我邁進這棟建築的那一刻，我就知道我要看到一些不得了的東西了，但是卻沒想到比我想象中還要厲害。每一件的精美都讓人合不攏嘴。對於細節的專註和創造力簡直難以形容。我太愛這裏了。哦對了，記得穿一件毛衣或者夾克，這裏空調開得很足，到最後我都冷得有些打顫了。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3825, 'lei k', 'https://www.tripadvisor.com.tw/Profile/leik', '我不好博物館,但這裡是例外,把名勝縮小,一下子到世界遊樂了.雖然博物館面積不大,但仔細去遊覽,他了不少時間,是一個有趣的景點.', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3826, '檸檬可樂', 'https://www.tripadvisor.com.tw/Profile/Getaway810753', '台北有許多的博物館和展覽館，袖珍博物館算是其中較特別的展館。需要買票才能入內觀賞。大部分都是縮小成12分之一的大小。不管是建物、風景、人物或蛋雕，都做得非常精緻。靠近點慢慢看，往往都會發現模型令人驚豔的小細節。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3827, 'Kriselle Rae D', 'https://www.tripadvisor.com.tw/Profile/645KrisD', '即使在谷歌地圖上也很難找到這個地方。它在一個建築群內，只有一個小的標誌，表明你在該地區的正確位置。博物館在地下室。你通過一個靠近電梯的門進入台灣的袖珍博物館。把你的票拿到鋪着地毯的地方，店員給你手上扣上印記。展品很不錯，深受微縮畫和玩偶屋愛好者的喜愛。我幾乎花了一整個下午去看從娃娃屋到城堡城鎮這些微縮模型的細節。至少可以說這些細節是精緻的。博物館商店也出售微縮畫甚至玩偶屋家居。絕對是一個獨一無二的博物館和一個在台北很棒的度過一個炎熱多雨的下午的方式。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3828, 'Washielim', 'https://www.tripadvisor.com.tw/Profile/Washielim', '我周四下午4點到6點，花了1.5小時呆在這裏。這是一個相對安靜的博物館，沒有擁擠和不體貼的吵鬧導遊的敘述。我很喜歡瀏覽和欣賞這些小型展覽品。遊客理解博物館禮儀。每個展覽箱都有一個故事。有來自不同國家，不同時代等的展覽箱。這是一個消磨午後時光的好地方。下午6點關門。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3829, 'Samuel S', 'https://www.tripadvisor.com.tw/Profile/SamuelS4630', '入場是二百元可以拍照禁止使用閃光燈，腳架和自拍棍 ，好的管理丫表揚，內容是模型有些是 人物故事有典古和歷史價值。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3830, 'Mei-Ching C', 'https://www.tripadvisor.com.tw/Profile/Compass734902', '之前帶學生參觀發現裡面驚喜無限.雖然都是縮小版的建築物或模型.但孩子們看得比我還仔細.而且都小心翼翼的深怕碰壞了這些珍貴的小物呢!!老師們都覺得是讓孩子們探索的好去處喔~', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3831, 'Pebbles821', 'https://www.tripadvisor.com.tw/Profile/Pebbles821', '對於那些對微縮模型，玩具屋，仿真模型感興趣的人，或者只是有一雙關注細節的眼睛或年輕的心的人，這裡是必須要看的！陳列品是由着名的微型工匠製作，主要來自美國，代表着非常精巧、高端的收藏。很多值得一看的，隨着一些真正令人驚嘆的展品進入高潮！我在這裏度過了超棒的一段時間，甚至我的丈夫和十幾歲的女兒並不是微型愛好者，也很享受。很不錯的禮品店，價格合理，有一個能坐下來休息的地方，如果你需要等待別人結束購物的話！', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3832, 'Michael Y', 'https://www.tripadvisor.com.tw/Profile/629michaely', '這個景點很隱蔽——它位於商業大樓的地下室，最初我們期望很低（因為它在辦公樓中看起來很渺茫）。但是，這裏值得一去。我和未婚夫和父母一起去，我們很喜歡這裏。在入口處，它展示了人們曾經玩過的舊玩具和娃娃，當你進一步走動的時候，有很多微型的十二分之一大小的微型模型相當有生活味。這些展品的範圍很大，從卧室，樹屋，平房，整個城堡的任何東西，我們相當震撼——質量並沒有隨着尺寸的減小而減少！我們花了約2個小時参觀這裏，走過了每一個展廳——你一定要來喲。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3833, 'Doralian', 'https://www.tripadvisor.com.tw/Profile/Doralian', '雖然展品久久才會更換一次，但第一次去一定會驚呼連連然後看很久很久，你一定會讚嘆製作的工藝居然能如此細膩，小小的世界蘊含大大的道理!', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3834, 'Yi Jung C', 'https://www.tripadvisor.com.tw/Profile/yijungc2016', '雖然票價不便宜，但是可以看到十分精細而費工的迷你模型，適合全家夏日在此吹冷氣消磨兩小時。裡面可以照相，建議將鏡頭盡量貼近玻璃，同時身穿黑色衣服避免反光。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3835, 'MstrViolinist', 'https://www.tripadvisor.com.tw/Profile/MstrViolinist', '隱藏在一個辦公樓的地下室，除非你去尋找它，否則你不知道它在那裡。裏面是一個令人難以置信的收集微縮模型，玩具屋，和小雕像的地方。許多錯綜複雜房間，收集品來自世界各地的許多不同的藝術家，顯然這是一個人的個人收藏', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3836, '櫻花水月相詩', 'https://www.tripadvisor.com.tw/Profile/DRAGONSAKURA', '適合帶全家人逛的景點，雖然要門票，但是花的會覺得很值得。不虛此行。逛完旁邊還有精品店可以看，裡面很多小飾品。 ', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3837, 'casabamelon77', 'https://www.tripadvisor.com.tw/Profile/casabamelon77', '博物館的入口比較破舊，門上缺字母。在裏面你可以看到很多的微縮模型，比如白雪，愛麗絲漫遊記等，還有古老英格蘭和愛爾蘭的建築等。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3838, 'garfieldHk', 'https://www.tripadvisor.com.tw/Profile/garfieldHk', '雖然不是一個大的博物館，但它是相當有趣的。創建這些小而精緻的項目是非常困難的。裏面沒有很多遊客，所以我可以花很長時間來欣賞每一處展覽。燈光有一些是關閉的，如果他們可以檢查一些微型的燈光，這個博物館會越來越好的。所以你來這的時候，不要在意這些小細節。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3839, 'broniac2016', 'https://www.tripadvisor.com.tw/Profile/broniac2016', '這是個很有趣的微型博物館。這裡有很多微型的玩具屋，這些玩具屋都很逼真，如果有時間去台北玩，厭倦了只有購物和享受美食的行程，這是一個值得一去的地方！', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3840, 'Thu H', 'https://www.tripadvisor.com.tw/Profile/490thuh', '我可以說什麼呢?這裏對於我來說就是天堂。這裏的一切都很完美。如果你是一個小型複製品的愛好者，記得要花半天的時間在這裏。但是 這裏不是最終的目的地。我怕老公覺得這裏一般般，孩子們特別是男孩都覺得很無聊。所以可能和女朋友或者是女兒來這裏？', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3841, 'waiemil', 'https://www.tripadvisor.com.tw/Profile/waiemil', '喜歡模型的便很適合來， 模型都是多的， 但對我來說如果時間有多才會來， 不是必到的參觀地點， 要購票入場， 及在地牢的。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3842, 'CzarEmmanuel', 'https://www.tripadvisor.com.tw/Profile/CzarEmmanuel', '除非你喜歡微縮模型（尤其是房子的微縮模型），否則你真得不會覺得這家博物館有趣。但是你若喜歡微縮模型，那你會覺得這家博物館很有趣，館內各種富有創意的微縮模型細節會給你留下深刻的印象。這家博物館很小，但這裏的收藏品彌補了這一缺陷。其中一些藏品根據主題布置展覽（比如根據童話故事敘述、音樂流派、歷史事件等）。我個人覺得這裏很有趣，雖然這地方很難找，門票費也很貴。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3843, 'marzner', 'https://www.tripadvisor.com.tw/Profile/marzner', '如果你對一些小東西很感興趣，那就参觀一下袖珍博物館。雖然這裏和其他袖珍博物館沒有太大的不同，但他們用郵票護照為一些主要展品提供了互動的一面。他們還舉辦了一個展覽，聲稱這是世界上最小的電視，並收集了大量以維多利亞時代歐洲和北美家庭內部裝飾為特色的微縮模型。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3844, 'Peter M', 'https://www.tripadvisor.com.tw/Profile/peterm930', '我挺享受参觀這裏，我能領會到製作這些模型需要多高的技藝，但我也發現，小孩子對這些模型都真的特別興奮，我認為這個地方對他們是最合適的。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3845, '나연아', 'https://www.tripadvisor.com.tw/Profile/Misspiikachu', '這個地方絕對是消磨時間的好地方。一些微縮模型質量非常好，而另一些只是普通模型。能看到不同的國家、不同的時期和一些電影真是太好了，尤其是如果你以前從未見過這樣的小場景的話。成人門票是新台幣200元。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3846, 'travel momomo', 'https://www.tripadvisor.com.tw/Profile/travelmomomo', '值得一看，地方不大，但放置了很多微縮模型，都是按照真品縮小了的，有一個全世界比例最小的樹上壙坑，是1比120的，另外還有一個全世界最小的電視機，有趣。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3847, 'ahliao', 'https://www.tripadvisor.com.tw/Profile/ahliao', '從地鐵站5號出口出來，步行大約8分鐘就可以到達這裏。博物館位於商業大樓的地下室。成人和兒童入的場費分別為200日元160日元。售票處在下午5點關閉，而博物館在下午6點關閉。他們還有一家出售微型显示器配件的商店。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3848, 'Jenny W', 'https://www.tripadvisor.com.tw/Profile/580jennyw', '展品算是美觀及多種類，但展品靜態為主，可互動的不多，展品內容需要家長解說，大概可消磨1小時，不適合小學生以下參觀。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3849, 'TripAdvisor 會員', '', '可能只是我對展品完全不感興趣，所以不太理解這樣一個博物館存在的意義及看點。可能是針對小朋友的吧。只看了10分鐘不到。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3850, 'eggchang', 'https://www.tripadvisor.com.tw/Profile/eggchang', '袖珍博物館裡面有櫥窗展示很多縮小版的東西, 每個櫥窗裡面都有小的解說牌, 別以為袖珍博物館就東西小而已, 其實每個櫥窗裡面的東西都很精緻, 真的很佩服製作的師傅', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3851, 'Isabella L', 'https://www.tripadvisor.com.tw/Profile/isabelloxlo', '這是一家小型博物館，展廳很小，但是展品眾多。你甚至不能仔細觀察每一件展品，因為展廳里有太多展品了。展廳里有各種類型的微小模型，包括古建築和不同時代的房子。如果你喜歡觀賞模型的話，你一定不虛此行。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3852, 'TripAdvisor 會員', '', '這個博物館還是很值得一去，裏面可以看到各種小玩具，地點位於地下B1層，這個有點不太好找，好在大廈外面有各種指示表，適合童心未泯的大人和帶小孩子去玩', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3853, 'jensrooi', 'https://www.tripadvisor.com.tw/Profile/jensrooi', '很小的博物館，主要功能的玩具屋。 只有幾個模型像格利佛遊記中拍的，所以微縮模型博物館就有點格格不入。 總的來說，這不是一個糟糕的地方，雖然我們只等了 20 分鐘看所有的展品雖然入場費是每人 200 新台幣。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3854, 'Jess W', 'https://www.tripadvisor.com.tw/Profile/jessw316', '博物館位於辦公大樓的地下室。 空間非常小和180 TWD入口是非常貴的。 我的觀點是如果你不是一個很大的風扇niniatures的,你應該把時間花在其他景點。 ', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3855, 'Eric C', 'https://www.tripadvisor.com.tw/Profile/NoCowsOnTheRoad', '這間博物館非常小。 最重要的是,這裏的展品似乎仍然住在20年前。 相比其他的博物館,入口費用太貴了。 就去他們的商店買一些小東西就足夠了。 試試這個地方如果你已經參觀了所有的其他旅遊景點都在臺北。', 'S0100', ' 袖珍博物館 Miniatures Museum of Taipei'),
(3856, 'Travellps', 'https://www.tripadvisor.com.tw/Profile/Travellps', '這裡常常有展覽，那天剛好下了大雨，趕在關門之前爬上了樓梯看到這片夕陽，真的很美。還有國家音樂廳與戲劇院，是個值得來逛逛的地方。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3857, 'TripAdvisor 會員', '', '天安門廣場大小相當，入口的劇院和音樂廳仿古建築單個都有太和殿一樣大。紀念堂像座山，我從側門進入樓梯內的底層部分，內部像商場一樣大，先参觀了中正先生生平物品紀念展，布展不吝面積，偉人之感油然而生。電梯到4樓是紀念堂正身，巨大中正先生銅像正襟危坐，目光望向地平線。造巨像確實有心理暗示效果讓人敬仰。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3858, 'Jake', 'https://www.tripadvisor.com.tw/Profile/Lucas-Taipei', '一進門就有左右音樂及戲劇兩廰院，正中是老蔣的紀念大廳，整體建築非常具有中國傳統特色，隨意逛逛休閑也適宜，看看老蔣的一些歷史也不錯，附近有吃的，離永康街很近，也近傳統市場，值得一游。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3859, 'Ching', 'https://www.tripadvisor.com.tw/Profile/yuching67', '交通方便，搭捷運即可抵達，園區寬廣，不論白天或晚上都可以來散步，晚上有憲兵交接（？）可以觀賞。另外還有國家劇院與音樂廳，都在這一區。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3860, 'Chin Chen', 'https://www.tripadvisor.com.tw/Profile/misschen_chin', '這兩天剛好有雙十花燈展出，還有現場演唱，真的很舒服。 只要天氣不太熱，不管是白天或晚上都很適合來中正紀念堂散步，朋友、家人、情侶或是遛狗遛小孩都很合適。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3861, 'Dom Toretto', 'https://www.tripadvisor.com.tw/Profile/Dom_Toretto_0425', '這裡是自由的象徵，美麗又大方的殿堂 民族熔爐的血汗，我們不會忘 兩側的藝術大廳，孕育著無數文化的傳承 我愛台灣，生日快樂！', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3862, 'niki tsai', 'https://www.tripadvisor.com.tw/Profile/nikitsai', '可去看衛兵交接和降旗,展覽室中有 先總統  蔣中正的座車(兩台勞斯萊斯)和各種勳章文物展，值得參訪 若行動不方便爬樓梯  ,也可搭電梯上下樓 ', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3863, 'h1234485', 'https://www.tripadvisor.com.tw/Profile/h1234485', '很多遊客來此.都把它當一個大公園.撇開國家音樂廳與戲劇廳不說.圍牆內有豐富的植物與魚池.主建築物中有碩大的蔣公銅像與定時的儀隊交接.但往往忽略的是樓下也有豐富的文物可以見證歷史.也不定期的舉辦各式展覽.值得一探究竟.', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3864, '董漢忠', 'https://www.tripadvisor.com.tw/Profile/CidTung', '雄偉的建築,顏色跟造型都是獨樹一格的地方，紀念堂內每整點會有衛兵的交接儀式，請務必要參與且記得給予軍人及國家元首該有的尊重，最近也很多人喜歡拍兩廳院的倒影，真的很美唷，白天晚上都很適合來的地方', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3865, 'aya', 'https://www.tripadvisor.com.tw/Profile/aya971104', '蹓小孩的好地方,內有國家音樂廳及不定期個別展覽,適合拎小朋友到處走走,增進知識的好地方,中正紀念堂內也有一些咖啡廳及小吃館,文創小店可以買,是個不錯踏青的好地方,', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3866, 'TechMarauder', 'https://www.tripadvisor.com.tw/Profile/TechMarauder', '我花了大約90分鐘在這裏参觀，並準點参觀了衛兵換崗。這是一個非常令人尊敬的儀式。這裏很棒，很適合拍照。夏天會非常熱，要做好準備。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3867, 'chuang,ming-i', 'https://www.tripadvisor.com.tw/Profile/Daydream802103', '腹地寬闊，建築有特色，兼具有歷史故事教育的地方。假日不想跑太遠，捷運出站就到，又不收門票，散步拍照晾小孩都不錯。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3868, 'vn46729oihoid', 'https://www.tripadvisor.com.tw/Profile/vn46729oihoid', '早上9點到下午5點，可在這看交接儀式。很舒服很大 風很舒服 另外五點10分可以看降旗，夕陽灑下 還是很美的 附近的杭州小籠包也好吃', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3869, 'Wawa', 'https://www.tripadvisor.com.tw/Profile/wwawaa', '中正紀念堂，建築雄偉，前面的廣場時常有不同的活動，無論是清晨、上午、下午、黃昏、夜晚…都各有其趣，在這裡發呆一整天，感受下台北市的日常，也非常有小確幸～', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3870, 'TSAI', 'https://www.tripadvisor.com.tw/Profile/penguineat', '中正紀念堂前方有一個很大的廣場，適合走走看看，夏天要注意太陽很大，晚上打燈觀看很漂亮，適合攝影人士取景練習', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3871, 'Katy Dang', 'https://www.tripadvisor.com.tw/Profile/Katyda1328', '中正紀念堂離我們住的酒店不太遠，走走就到，而且附近也有捷運。有很多景點參觀，可以走到自由廣場。自由廣場和中正紀念堂是通的，四樓有蔣中正的銅像，每一個小時的整點都會有禮兵交接。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3872, '許戎和', 'https://www.tripadvisor.com.tw/Profile/Adventurer810232', '在暑假炎熱的早上，來到充滿文藝氣習的地方，有水池，有迴廊，更有腹地廣擴的廣場，想在這聽聽音樂也行，看戲劇也行，更可以溜小孩，偶爾可餵魚，欣賞各種花草，小鳥，松鼠，是在都市叢林的我們可隨時去溜溜的地方。真的很方便。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3873, '介正劉', 'https://www.tripadvisor.com.tw/Profile/Scenic808087', '       好久没到中正紀念堂參觀了，開完會距晚餐還有時間，就到這邊參觀地面層，這時正展各種彩色藝術大魚，及幾可亂真的人体雕刻，超寫實且多元化生活情境，中正紀念堂佔地寬闊很多人在這邊散步。不定時會有一些市集，很熱鬧。如果要吃東西，裡面也提供多元化看起來就不錯吃的餐點。中正紀念堂外面人工造景定期專人整理，花草樹木都保護得極佳狀態，吸引各國許多遊客來台必遊景點。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3874, '914L', 'https://www.tripadvisor.com.tw/Profile/914L', '演藝廳參加幼稚園畢業典禮。每到六月，幾乎天天都有學校報到。場地很不錯，結束後走到戶外還看到很多松鼠。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3875, 'Melissa', 'https://www.tripadvisor.com.tw/Profile/MelissaLitUp', '白天與晚間不同氛圍，推薦可以都嘗試看看，人像照建議可趁白天光線充足，與紅花綠葉一起搭配廣場上的拱門及音樂廳的飛檐一同入景，傍晚點燈後俯瞰頗為壯麗，別有一番風情，內部館區也有具歷史意義的展覽可以免費觀賞，適合納入觀光行程。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3876, 'Sindy T', 'https://www.tripadvisor.com.tw/Profile/sindyt263', '捷運一出就到，好大的廣場，可以了解中華民國在台灣的故事，逗留時間約45分鐘就好了，可以好好拍照，適合長者及小朋友參觀。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3877, '張結偉', 'https://www.tripadvisor.com.tw/Profile/KitWaiCheung', '今次是第二次到來參觀中正紀念堂閱兵，每次看到都覺得他們整齊及有紀律。並可以參觀台灣的人民對國家的專重及齊心。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3878, 'Paulo S', 'https://www.tripadvisor.com.tw/Profile/PauloS6729', '小孩放寒假真的是給媽媽們的功課😂😂 每天家裏屋頂快要掀開了✨✨ 4歲哥和1歲妹✨✨ 早上起床-相親相愛2分鐘❤️ 兄妹打架一整天👦🏻👧🏻 要出去玩，瞬間又兄妹團結一致，對抗媽媽！ #小孩心好難懂 #1打2 #台北快閃一日遊 ', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3879, 'TripAdvisor 會員', '', '紀念堂如蔣中正的字一樣，中正威武。我們到樓上的時候，剛巧遇到儀式剛剛開始。不知道為什麼，可能觸碰到了記憶之中的哪裡，當口號響起的時候，自己忍不住淚目，可能想起革命先烈們的捨生忘死，可能是感慨蔣中正的委屈，五味雜陳不可分辨。無論如何，慶幸來到了這裏。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3880, 'yangjun8882008', 'https://www.tripadvisor.com.tw/Profile/yangjun8882008', '很有歷史感的地方，每天很多遊客過來參觀，看看蔣中正的一些歷史事蹟，紀念一下當時的那段歷史，看看直接做過的事情。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3881, 'Christine Liu', 'https://www.tripadvisor.com.tw/Profile/Traveler_MLL', '有著戲劇院和音樂廳及書店、餐廳以及大廣場的中正紀念堂是散步看表演和聽音樂會的好去處，有空時很適合去走走逛逛，廣場上有時會舉辦活動。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3882, 'maggiek2016OY', 'https://www.tripadvisor.com.tw/Profile/maggiek2016OY', '#中正紀念堂 #兒時回憶 涼風徐徐吹來 是個很適合散步踏青的地方 平時忙碌不堪 只有轉程接駁時才會來的中正紀念堂 今天的天氣真的變得像青島ㄧ般的涼爽宜人', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3883, 'AnitaCCTW', 'https://www.tripadvisor.com.tw/Profile/AnitaCCTW', '空間寬敞舒適，松鼠、鳥群、麻雀、魚類，帶小孩來，可以在魚池旁買投幣魚飼料餵魚、鴿子，玩上半天不是問題，傍晚還有降旗儀式，看到高大帥氣的軍人隊伍踏著整齊的步伐，時間允許的話千萬別錯過。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3884, 'Glens613', 'https://www.tripadvisor.com.tw/Profile/Glens613', '巨大的美麗園景花園，結構驚人。以歷史文物共同構成。我們也很欣賞這裡有一個非常好的餐廳，你可以在該地區漫步后享用美食。由於地鐵站就在紀念館旁邊，因此來這裏非常方便。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3885, 'Claire', 'https://www.tripadvisor.com.tw/Profile/molkon', '帶過許多外國朋友來這裡，大家都表示很喜歡，建議可以在下午的時候到來，先拍些照片，然後在附近吃個東西或喝杯咖啡，再返回來拍夜景，完全不同風格，但都很美。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3886, '王敏芬', 'https://www.tripadvisor.com.tw/Profile/wmf2019', '位在台北市中正區的中正紀念堂是一個國內外都很知名的觀光景點之一，裡面也有莊嚴的憲兵可以看他們在衛兵交接阿', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3887, 'Jacky', 'https://www.tripadvisor.com.tw/Profile/jjkk1028', '非常大的腹地，有很多假日活動，很多有趣的是會在這邊發生，假日的時候過來散散步，一切都覺得很美好，兩廳院也在這邊。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3888, '惠芳 張', 'https://www.tripadvisor.com.tw/Profile/Daydream708648', '位於市中心到中正紀念堂交通非常方便 搭捷運是最方便 廣闊的空間，是很多社團課後活動練習好場地 館內有不定期的展覽。非常棒的展覽 這裡也是附近居民運動場所 帶小孩出門遊玩的好地方（可以買魚飼料 餵餵魚）', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3889, '旅行在路上', 'https://www.tripadvisor.com.tw/Profile/Trail809346', '這次肚子來台北，抽空去參觀中正紀念堂。需要爬上高高的台階才能到達。有人很多，但是大家都很講秩序，不過這裡的衛生間不太好找。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3890, 'hekotenbui', 'https://www.tripadvisor.com.tw/Profile/Tourist810182', '很棒的觀光景點!衛兵交接也很有趣，周邊設施也很好,建議來台灣旅遊一定要來造訪!園區內的庭園也很棒，有很多松鼠可以近距離觀察!', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3891, '萬里路', 'https://www.tripadvisor.com.tw/Profile/PPKY2018', '如果要來參觀的話，奉勸大家要做足準備。。因為大部分的地方都在戶外，而且四周沒有高樓。夏天會曬死，冬天會凍死！ 如要看換兵的話，緊記要看看時間。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3892, 'where1009', 'https://www.tripadvisor.com.tw/Profile/where1009', '太熱的景點，清涼的地方只要建築物內，建築物內有一種奇怪的味道。最多人的地方是販賣紀念品的店！ 假日時左右兩棟表演的場地屋簷下，有許多熱血青年正在練習曲跳舞，熱情洋溢。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3893, 'fly760424', 'https://www.tripadvisor.com.tw/Profile/fly760424', '這個地方的歷史很有趣，占地蠻大的，假日的時候會看到很多的學生們在這邊練舞或是玩滑板之類的，是個很有活力的地方', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3894, 'fritzie18', 'https://www.tripadvisor.com.tw/Profile/fritzie18', '這裏講述台灣的歷史。幸運的話你可以見證每小時一次的看守人交接。這裏的景色也很好。通過地鐵綠色線中正紀念堂站可以輕鬆到達這裏。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3895, 'boobam8876', 'https://www.tripadvisor.com.tw/Profile/boobam8876', '難得在台北市有個大空地，有任何遊行聚會都會在這，對很多不同世代的人，都很有記憶點，也許當初是充滿政治意涵，現在已與過去不同', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3896, 'RogersEm', 'https://www.tripadvisor.com.tw/Profile/RogersEm', '我的媽媽對中正堂尤其感興趣，因此來到台北，她必去中正堂。花園令人印象深刻，我們到的時候下雨，無法真正停下來欣賞。衛兵換崗相當出色，但是我很高興至少見過一次。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3897, 'mylau18', 'https://www.tripadvisor.com.tw/Profile/mylau18', '紀念堂佔地面積廣闊，挺開揚宏偉的，看到很多小朋友在放電。當天正值櫻花盛開季節，紀念堂也有幾株小小的櫻花。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3898, '392pandac', 'https://www.tripadvisor.com.tw/Profile/392pandac', '就在捷運站旁邊，有時間可一遊！嚟主要是看展覽，到訪當日有安廸華荷！如首次到訪可搭電梯上樓睇蔣介石像！', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3899, 'Zhao Hui', 'https://www.tripadvisor.com.tw/Profile/winnieal', '吃完金峰魯肉飯就來走走，廣埸夠大，雖然到處都是遊客，但也不算太濟湧，捷運又有出口，非常方便，首次到台灣必遊景點。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3900, 'Expedition608830', 'https://www.tripadvisor.com.tw/Profile/Expedition608830', '這是一個失敗的建物 都市之瘤 裏面供奉著屠殺台灣人的獨裁者 只有奴才供養的邪靈存在 不會是個正面的力量 台灣人覺醒了 就會拆除  ', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3901, '介正劉', 'https://www.tripadvisor.com.tw/Profile/Scenic808087', '    好久沒帶兒子出來遊玩，此次藉由吃飯之便，順便到中正紀念堂，一賞雨後黃昏的中正紀念堂。還是一樣的建築花草佈置，但在涼風徐徐，天色有點暗又不太暗的背景下，另外有一番寧靜美麗祥和的氣氛，遊客很少但卻很國際化，有歐美白人，也有來自亞洲各國的人。大廣場正在搭鷹架，好像準備明日的大型活動，來到中正紀念堂廣場，整體的花草 建築及寬廣的水泥地，還是非常的美麗。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3902, 'Felixho1017', 'https://www.tripadvisor.com.tw/Profile/Felixho1017', '整個空間十分廣闊，前往亦十分方便，在中正紀念堂下捷運，但建議搽防曬前往，並且會有點熱，00分會有換兵，十分震撼。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3903, 'KUANG0120', 'https://www.tripadvisor.com.tw/Profile/KUANG0120', '是個寬廣的活動空間，親子、好友、情侶都適合在這邊散散步、做做運動、聊聊天，同時也不會太吵，假日休閒的好去處。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3904, 'Felix A', 'https://www.tripadvisor.com.tw/Profile/felixa455', '景點還不錯，我們可以看到衛兵換崗，寺廟和兩座建築物。邊上是一個小公園。我可以呆在那裡一整天，只是陽光太刺眼！', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3905, 'Sheeplee1987', 'https://www.tripadvisor.com.tw/Profile/Sheeplee1987', '走到最上面可以看衛兵交接(主要看點)，週邊有賣些文創商品、輕食、咖啡館。外為也有些人繞著圈慢跑，位置離捷運超近。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3906, '帕 林', 'https://www.tripadvisor.com.tw/Profile/Seaside775043', '國共內戰,國民黨敗。蔣中正領軍,於台灣建國民政府,統治台灣數十載。 冷戰,美蘇對抗。美為防共,支持台灣;蘇為抗美,支援大陸。 暗殺與諜戰;毛澤東與蔣中正較勁。當中可怕,當中不安,文字沒法形容。 後冷戰的今天,兩岸關係緩和。欲曉其可怕不安,只能進中正紀念堂,觀其展品。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3907, '安琦 林', 'https://www.tripadvisor.com.tw/Profile/Footprints771085', '我們到達的時候下雨了，但也被中正紀念堂的牌坊震撼了。因為它真的很宏偉。在內有些茶坊讓遊客參與。可惜的是，小孩子對這地方沒太大興趣，結果連換班儀式也沒看就走了。下次要等孩子高小以上再來一次。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3908, 'Tethys T', 'https://www.tripadvisor.com.tw/Profile/602tethyst', '台北的著名景點，是一個很大的廣場，來這邊的遊客好像是中年人比較多。整點有衛兵的交接表演可以觀賞，建議早一點來佔個有利位置觀看，如未來過的話不妨一來。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3909, '維 子', 'https://www.tripadvisor.com.tw/Profile/Trek809848', '一個為了紀念獨裁者而生的公園， 而且還是仿製中國帝王陵寢所蓋的， 個人覺得這個紀念堂言過其實，我認為旁邊的國家歌劇院和國家戲劇院，都要比中正紀念堂本身的文化意義和本質要來的重要。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3910, 'lei k', 'https://www.tripadvisor.com.tw/Profile/leik', '中正紀念堂就如台北的象徵一樣,一般第一次到台北必定會去的景點.這裡感覺莊嚴安靜,有已故總統的資料在此供參觀. 如果能在合適時間到來,可以見証步兵交接,是另一個節目.', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3911, 'YOHIKOSHI', 'https://www.tripadvisor.com.tw/Profile/YOHIKOSHI', '除了禮兵的表演，或者是兩旁的表演廳觀賞表演，這裡其實沒有什麼好晃的！來一次就夠了！其他都還好！不過如果懂建築的話，那邊的建築是有考究的，可以細觀還蠻有趣的。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3912, '恆旭 潘', 'https://www.tripadvisor.com.tw/Profile/Escape431081', '空曠的廣場是散步的好所在，年輕人對中正較為冷感了，歷史的是非功過是執政的人在定義，但是成王敗寇總是必然的定律。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3913, '134caroll', 'https://www.tripadvisor.com.tw/Profile/134caroll', '對帶着小小孩來說，只能說到此一遊而已。主要等換兵時間，看看士兵步操。但孩兒太小等得太久沒有耐性，不怕等待的看看換兵儀式還可以吧！  ', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3914, 'ling0606', 'https://www.tripadvisor.com.tw/Profile/ling0606', '魚池適合帶小孩同行，觀察錦鯉、烏龜及水鴨，園內植物多樣，四季都有不同的花朵綻放，春天賞櫻、秋天賞楓。主展覽館不定期有各式各樣展覽，可供參觀。兩院廳的演出也值得一看。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3915, 'ishy945', 'https://www.tripadvisor.com.tw/Profile/ishy945', '近距離了解中正先生，開眼界了。 算是一代偉人，成王敗寇而已，參訪的人不算多，哨兵換崗挺有趣的，值得看看。 祝願他的家人也會好！', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3916, '54092', 'https://www.tripadvisor.com.tw/Profile/54092', '13年前往中正紀念堂，氣氛莊嚴四周展出 ，蔣介石先生的歷史 ，現在重遊故地發現已變成一個商品市場，真是有點失望', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3917, 'Desmond L', 'https://www.tripadvisor.com.tw/Profile/dmanlai325', '傍晚時份的景色好美，射燈照射到自由廣場的門面顯得份外有氣勢。中正廣場好大好廣闊，走得爸媽腿酸了。中正紀念堂的入口就可以見到蔣先生的石像，特别顯得莊嚴。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3918, 'CarManAlex', 'https://www.tripadvisor.com.tw/Profile/CarManAlex', '大忠門及大孝門是主要入口 但也成了遊客 參觀動線的衝突 有了展覽品 卻沒有紀念品的銷售？ 很矛盾的地方。 整點鐘 去樓上看衛兵交接  電梯的出入口 是衛兵也是遊客必搭的  ', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3919, '際健 林', 'https://www.tripadvisor.com.tw/Profile/Global809590', '台灣人忘了去尊敬對台灣有重要貢獻的蔣中正總統。一個莊嚴肅穆的紀念館，一直被抹去蔣總統的品格。一個大中至正的牌坊，硬是被換成了自由廣場，完全失去了一個高度的地標。對觀光的重要因素正一再的被傷害。所以，這紀念堂失去了過去的光彩。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3920, '798mike', 'https://www.tripadvisor.com.tw/Profile/798mike', '每天上班前都會繞個一二圈, 早上晨起做活動的人很多, 人氣很旺, 園內花草也照顧的很好,但警衛應該要常巡視, 不是只待在崗裡, 很多晨起活動的團體, 佔據了大半個人行道, 走過時還怕會被揮到...特別是在近杭州南路那一段...', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3921, 'ShihPin', 'https://www.tripadvisor.com.tw/Profile/ShihPin', '以台北市而言，自由廣場是個相當大的休閒廣場。而不論好壞、喜惡如何，可以褒、可以貶，但不可否認的，建築物本身就是確確實實記錄了一段曾經真實存在於台灣的歷史，光就此點，就值一看。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3922, '行者漫遊', 'https://www.tripadvisor.com.tw/Profile/Navigator811068', '遠從外國到訪的遊客一定要來看看。它有著它的文化價值及歷史背景，而夜晚又是諸多喜歡跑步、健身的好地方。因為…夠大。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3923, 'TAIWAN104', 'https://www.tripadvisor.com.tw/Profile/TAIWAN104', '1.中國客好像變少了，人沒以前多。 2.常常舉辦一些活動，非常熱鬧 3.要走到最上面其實蠻累的，但風景很好。 ', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3924, 'mr_badtzmarux', 'https://www.tripadvisor.com.tw/Profile/mr_badtzmarux', '地方很大, 建議預留半天至一天遊覽, 是台灣著名地標之一, 很值得參觀, 令人印象深刻, 因為有著美麗的庭院包圍, 是一個很適合旅客的好地方。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall'),
(3925, 'mr_badtzmarux', 'https://www.tripadvisor.com.tw/Profile/mr_badtzmarux', '這是一個旅遊人仕很值得去參觀的地方, 場地很大, 也會進行交接儀式, 是一個很特色的地方, 建議預留半天遊覽。', 'S0101', ' 中正紀念堂 Chiang Kai-Shek Memorial Hall');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `user_comment`
--
ALTER TABLE `user_comment`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `user_comment`
--
ALTER TABLE `user_comment`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3926;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
