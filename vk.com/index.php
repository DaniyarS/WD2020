<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Добро пожаловать</title>
  <link rel="stylesheet" type="text/css" href="css/main.css">
</head>

<body>
<header>
  <div id="wrapperHeader">
    <div id="logotype"></div>
    <input type="text" id="search" placeholder="Поиск">
    <div id="SwitchToEng">Switch to English</div>
  </div>
</header>
<div id="main">
    <div id="mobileVersion">
        <div id="title" >ВКонтакте для мобильных устройств</div>
        <div id="subtitle"> Установите официальное мобильное приложение ВКонтакте и оставайтесь в курсе новостей Ваших друзей, где бы Вы ни находились.</div>
        <div id="android" onClick="downloadAndroidVersoion()">
						<div id="download"><div id="logo"></div>VK для Android</div>
					</div>
						<div id="ios" onClick="downloadIosVersoion()">
							<div id="download"><div id="logo"></div>VK для iPhone</div>
						</div>
					<div id="wp" onClick="downloadWpVersoion()">
						<div id="download"><img src="images/icoWp.png" id="WindowsPhone" alt="">VK для WP</div>
					</div>
    </div>
    
    <div id="rightsight">
        <div id="authorizationForm">
            <input type="text" id="login" placeholder="Телефон или email">
            <input type="password" id="password" placeholder="Пароль">
            <button id="finishAuthorization">Войти</button>
            <div id="restorePass"><a href="#">Забыли пароль?</a></div>
        </div>
        <div id="registrationForm">
            <div id="title" >Впервые ВКонтакте?</div>
            <div id="subtitle">Моментальная регистрация</div>
            <input type="text" name="nameUser" id="nameUser" placeholder="Ваше имя">
            <input type="text" name="surnameUser" id="surnameUser" placeholder="Ваша фамилия">
            <span id="birthdayTitle">Дата рождения: </span>
            <?php include('datelist.php'); ?>
            
            
            <div id="button"><input type="button" id="registrationButton" value="Продолжить регистрацию"/></div>
            
            <div id="button1"><input type="button" id="registrationButton1" value="Войти через Facebook"/></div>
           
            </div>  
            <div class="clear"></div>
    </div>
    <footer>
        <div id = "aboutVK"> <a href="#">Вконтакте</a> &copy; <?php echo date("Y"); ?></div>
        <div id="smth">
            <a href="#" target='_blank'>О Вконтакте</a>
            <a href="#" target='_blank'>Правила</a>
            <a href="#" target='_blank'>Реклама</a>
            <a href="#" target='_blank'>Разработчикам</a>
        </div>
        
        <div id="lang">
            <a href="#">Русский</a>
            <a href="#">Українська</a>
            <a href="#">English</a>
            <a href="#">все языки »</a>
        </div>
    </footer>
</div>
</body>
</html>
