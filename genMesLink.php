<?php 

require "MessageService.php";

    if (isset($_POST['encryptText'])) {
        $messageText = $_POST['encryptText'];
        $messageService = new MessageService();
        echo $messageText;

        $messageService->saveMessage($messageText);
    }
    else {
        echo "Please enter a message";
    }

?>