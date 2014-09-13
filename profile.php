<html>
<head>
	<title>Save the Net--Your Profile</title>
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap-theme.min.css">
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
	<script type="text/javascript" src="bootstrap/js/bootstrap.min.js"></script>
	<script type="text/javascript" src="jquery-2.1.1.min.js"></script>
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
          <button type="button" class="btn btn-default navbar-btn" onclick="LogoutFacebook()">Log Out</button>
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

	<div id="left-panel">
		<h3>Your Profile</h3>

	</div>
	<div id="center-panel">
		<h3>Take Action</h3>

	</div>
	<div id="right-panel">
		<h3>Learn More</h3>

	</div>
</div>

<script type="text/javascript">
	window.fbAsyncInit = function() {
	  FB.init({
	    appId      : '692319020856556',
	    cookie     : true,  // enable cookies to allow the server to access 
	                        // the session
	    xfbml      : true,  // parse social plugins on this page
	    version    : 'v2.1' // use version 2.1
	  });

	function LogoutFacebook() {    
		FB.logout(function (response) {
    	location.href = "logout.php"
	});   }

	// function statusChangeCallback(response) {
 //    console.log('statusChangeCallback');
 //    console.log(response);
 //    // The response object is returned with a status field that lets the
 //    // app know the current login status of the person.
 //    // Full docs on the response object can be found in the documentation
 //    // for FB.getLoginStatus().
 //    if (response.status === 'connected') {
 //      // Logged into your app and Facebook.
 //      //testAPI();
 //      location.href = "profile.php"
 //    } else if (response.status === 'not_authorized') {
 //      // The person is logged into Facebook, but not your app.
 //      document.getElementById('status').innerHTML = 'Please log ' +
 //        'into this app.';
 //    } else {
 //      // The person is not logged into Facebook, so we're not sure if
 //      // they are logged into this app or not.
 //      document.getElementById('status').innerHTML = 'Please log ' +
 //        'into Facebook.';
 //    }
 //  }

 //  function checkLoginState() {
 //    FB.getLoginStatus(function(response) {
 //      statusChangeCallback(response);
 //    });
 //  }
</script>
</body>
</html>