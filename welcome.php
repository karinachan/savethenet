<?php

session_start();

if( isset( $_SESSION['visits'] )) {
    $_SESSION['visits']++;
 } else {
    $_SESSION['visits'] = 1;
 }

require_once("MDB2.php");
require_once("/home/cs304/public_html/php/MDB2-functions.php");

// The following defines the data source name (username, password,
// host and database).

require_once('wmdb-dsn.inc');

// The following connects to the database

$dbh = db_connect($wmdb_dsn);

$sql = "SELECT tt,title FROM movie WHERE title <> '' ORDER BY title LIMIT 100";
$resultset = query($dbh,$sql);

$self = $_SERVER['PHP_SELF'];

pageheader('Movie Shopping');
echo "<body>\n";

if( $_SESSION['visits'] > 1 ) {
    echo "<p>Welcome back!  You've visited " . $_SESSION['visits'] . " times.\n";
 } else {
    echo "<p>Welcome! This page allows (will allow) you to order movies.\n";
 }

$show = 'show cart';
print "<form method='post' action='$self'><input type='submit' name='submit' value='$show'></form>\n";

if( isset($_POST['submit']) && $_POST['submit'] == $show ) {
    showcart();
 }

if( isset($_POST['tt']) ) {
    addtocart($_POST['tt'],$_POST['title']);
    showcart();
 }


echo "<ol>\n";
while($row = $resultset->fetchRow(MDB2_FETCHMODE_ASSOC)) {
    $tt = $row['tt'];
    $title = htmlspecialchars($row['title'], true);
    echo "<form method='post' action='$self'><div class='form_body'>" .
        "<li><input type='hidden' name='tt' value='$tt'>" .
        "<input type='hidden' name='title' value='$title'>\n" .
        "<input type='submit' value='add to cart'> $title </div></form>\n";
}
echo "</ol>\n";

function pageheader($title) {
    echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
<head>
';
    echo "<title>$title</title>";
    echo '
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name=author content="Scott D. Anderson">
<link rel="stylesheet" type="text/css" href="../webdb-style.css">
<style type="text/css">
  div.form_body { display: inline; }
</style>
</head>
';
}

function addtocart($mid,$mtitle) {
    echo "<p>Thanks for ordering <strong>$mtitle</strong> ($mid); we'll record your order.\n";
    # I'm gluing 'tt" onto the front of the key, just for clarity.  The
    # value is the number of copies.
    if (isset($_SESSION["tt$mid"]) ) {
        $_SESSION["tt$mid"]++;
    } else {
        $_SESSION["tt$mid"] = 1;
    }
    # In this fancy version, I'm also recording the name of the movie
    $_SESSION["title$mid"] = $mtitle;
}

function showcart() {
    print "<p>Your cart has \n<ul>";
    foreach( $_SESSION as $key => $value ) {
        if( substr($key,0,2) == 'tt' ) {
            # This is a movie id, the value is the number of copies
            # Let's look up the movie title, by replacing tt with title
            $key2 = 'title' . substr($key,2);
            $title = $_SESSION[$key2];
            if( $value == 1 ) {
                print "<li>$key ($title) one copy\n";
            } else {
                print "<li>$key ($title) $value copies\n";
            }
        }
        print "</ul>\n";
    }
}

?>
</body>
</html>
