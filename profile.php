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
          <span id="fbLogout" onclick="fbLogout()"><a class="fb_button fb_button_medium btn btn-default navbar-btn"><span class="fb_button_text">Logout</span></a></span>
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

<script type="text/javascript">
	window.fbAsyncInit = function() {
	  FB.init({
	    appId      : '692319020856556',
	    cookie     : true,  // enable cookies to allow the server to access 
	                        // the session
	    xfbml      : true,  // parse social plugins on this page
	    version    : 'v2.1' // use version 2.1
	  });

	<script>
function fbLogout() {
        FB.logout(function (response) {
            //Do what ever you want here when logged out like reloading the page
            window.location.reload();
        });
    }
</script>


</body>
</html>