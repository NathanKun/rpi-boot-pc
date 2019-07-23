<?php
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>CatPC Boot</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
	<form action="./" method="post">
		<input type="submit" name="action" value="Boot">
		<input type="submit" name="action" value="Reboot">
	</form>
</body>
</html>
<?php
} else if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	$secret = 'somesecret';
	$rpi = "192.168.1.???";
	if(isset($_POST['action'])) {
		if ($_POST['action'] === 'Boot') {
			echo file_get_contents("http://" . $rpi . "/boot?secret" . $secret);
		} else if ($_POST['action'] === 'Reboot') {
			echo file_get_contents("http://" . $rpi . "/reboot?secret" . $secret);
		}
	} else {
		echo "no action specified";
	}
}
