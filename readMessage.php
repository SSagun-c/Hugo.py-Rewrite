<?php
require "MessageService.php";




if (isset($_GET['id'])) {
    $id = $_GET['id'];
    $messageService = new MessageService();

    $servername = "localhost";
    $username = "Colin";
    $password = "colin";

    try {
        $conn = new PDO("mysql:host=$servername;dbname=message", $username, $password);
            // set the PDO error mode to exception
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $stmt = $conn->prepare("SELECT id, message FROM messages WHERE id="."'".$id."'");
        $stmt->execute();

        $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
        foreach($stmt->fetchAll() as $value) {
            echo "<div>";
            echo "here is your wonderful message<br>";
            echo $value["message"];
            echo "</div>";

        }
    $messageService->deleteMessage($id);
    } catch(PDOException $e) {
        echo "Error: " . $e->getMessage();

    }
    $conn = null;
}

?>