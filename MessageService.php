<?php




    class MessageService { 
        private $connection = NULL;

        function __construct() {
            $servername = "localhost";
            $username = "Colin";
            $password = "colin";

            $this->connection = new PDO("mysql:host=$servername;dbname=message", $username, $password);
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        }
        public function deleteMessage($id) {
            try {
                $sql = "DELETE FROM messages WHERE id="."'".$id."'";
        
                // use exec() because no results are returned
                $this->connection->exec($sql);
                echo "Your message was deleted";
                }
            catch(PDOException $e) {
                echo "Error: " . $e->getMessage();
            }
        }

        public function saveMessage($messageText) {
            try {
                $stmt = $this->connection->prepare("INSERT INTO messages (message, id) VALUES (:message, :id)");
                $stmt->bindParam(':message', $message);
                $stmt->bindParam(':id', $id);

                $message = $messageText;
                $id = uniqid();
                $stmt->execute();

                echo "<a href='http://localhost/test/readMessage.php?id=".$id."'>Your generated Link here:</a>";
            }
            catch(PDOException $e) {
                echo "Error" . $e->getMessage();
            }
        }
    }




?>