//include the Facebook PHP SDK
include_once 'facebook.php';

//instantiate the Facebook library with the APP ID and APP SECRET
$facebook = new Facebook(array(
    'appId' => '692319020856556',
    'secret' => 'be169eb088af12c4760f53d460cb978a',
    'cookie' => true
));

//Get the FB UID of the currently logged in user
$user = $facebook->getUser();

//if the user has already allowed the application, you'll be able to get his/her FB UID
if($user) {
    //do stuff when already logged in
} else {
    //if not, let's redirect to the ALLOW page so we can get access
    //Create a login URL using the Facebook library's getLoginUrl() method
    $login_url_params = array(
        'scope' => 'publish_stream,read_stream,offline_access,manage_pages',
        'fbconnect' =>  1,
        'redirect_uri' => 'http://'.$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']
    );
    $login_url = $facebook->getLoginUrl($login_url_params);

    //redirect to the login URL on facebook
    header("Location: {$login_url}");
    exit();
}
