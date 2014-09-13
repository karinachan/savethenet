<html>
<head>
	<title>Save the Net--Your Profile</title>
	<script type="text/javascript" src="bootstrap/js/jquery-2.1.1.min.js"></script>
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap-theme.min.css">
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
	<script type="text/javascript" src="bootstrap/js/bootstrap.min.js"></script>
	
	<link rel="stylesheet" type="text/css" href="profile.css">
</head>
<body>
<div id="container">

	<!-- NAVBAR --> 
	<nav class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navnav">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Save the Net</a>
        </div>
        <div class="collapse navbar-collapse" id="navnav">
          <span id="fbLogout" onclick="logoutFB()"><a class="fb_button fb_button_medium btn btn-default navbar-btn"><span class="fb_button_text">Logout</span></a></span>
        </div>
      </div>
    </nav>

    <!-- END NAVBAR --> 

    <!-- ALERT -->
    <div class="alert alert-danger fade in" role="alert">
      <button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
      <h4>Don't Miss Your Chance to Take Action</h4>
      <p>The FCC closes comments on the proposed rules on Monday, September 15th!</p>
      <button type="button" class="btn btn-danger" id="send-comment" onclick='location.href="http://act.freepress.net/sign/internet_fcc_nprm_oliver?source=takeaction"'>Send a Comment Now!</button>
      </p>
    </div>
    <!-- END ALERT -->

	<div id="left-panel" class="content-panel">
		<h3>Your Profile</h3>

	</div>
	<div id="center-panel" class="content-panel">
		<h3>Take Action</h3>

	</div>
	<div id="right-panel" class="content-panel">
		<h3>Learn More</h3>

	</div>
</div>

<script>
  // This is called with the results from from FB.getLoginStatus().
  function statusChangeCallback(response) {
    console.log('statusChangeCallback');
    console.log(response);
    // The response object is returned with a status field that lets the
    // app know the current login status of the person.
    // Full docs on the response object can be found in the documentation
    // for FB.getLoginStatus().
    if (response.status === 'connected') {
      // Logged into your app and Facebook.
      //testAPI();
      //location.href = "profile.php"
    } else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into this app.';
    } else {
      // The person is not logged into Facebook, so we're not sure if
      // they are logged into this app or not.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into Facebook.';
    }
  }

  function statusChangeCallback2(response) {
    console.log('statusChangeCallback');
    console.log(response);
    // The response object is returned with a status field that lets the
    // app know the current login status of the person.
    // Full docs on the response object can be found in the documentation
    // for FB.getLoginStatus().
    if (response.status === 'connected') {
      // Logged into your app and Facebook.
      //testAPI();
      //location.href = "profile.php"
      console.log("YOU FUCKED UP");
    } else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      console.log("FACEBOOK FUCKED UP");
    } else {
      // The person is not logged into Facebook, so we're not sure if
      // they are logged into this app or not.
      location.href = "logout.php";
    }
  }

  // This function is called when someone finishes with the Login
  // Button.  See the onlogin handler attached to it in the sample
  // code below.
  function checkLoginState() {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }

  window.fbAsyncInit = function() {
  FB.init({
    appId      : '692319020856556',
    cookie     : true,  // enable cookies to allow the server to access 
                        // the session
    xfbml      : true,  // parse social plugins on this page
    version    : 'v2.1' // use version 2.1
  });

  // Now that we've initialized the JavaScript SDK, we call 
  // FB.getLoginStatus().  This function gets the state of the
  // person visiting this page and can return one of three states to
  // the callback you provide.  They can be:
  //
  // 1. Logged into your app ('connected')
  // 2. Logged into Facebook, but not your app ('not_authorized')
  // 3. Not logged into Facebook and can't tell if they are logged into
  //    your app or not.
  //
  // These three cases are handled in the callback function.

  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });

  };

  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));

  // Here we run a very simple test of the Graph API after login is
  // successful.  See statusChangeCallback() for when this call is made.
  function testAPI() {
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me', function(response) {
      console.log('Successful login for: ' + response.name);
      document.getElementById('status').innerHTML =
        'Thanks for logging in, ' + response.name + '!';
    });
  }

  function logoutFB() {
    FB.getLoginStatus(function(response) {
    FB.logout(function(response) {
        // Person is now logged out
        console.log("YAY");
    });
    statusChangeCallback2();
  });
      }

    </script>


</body>
</html>