<?php

/* https://api.telegram.org/bot5914175010:AAHGRNHJaeAyZmZNkGGAZRJNi0I28zw8Ebk/getUpdates,
где, XXXXXXXXXXXXXXXXXXXXXXX - токен вашего бота, полученный ранее */

$name = $_POST['user_name'];
$phone = $_POST['user_phone'];
$header = $_POST['user_header'];
$message = $_POST['user_message'];
$token = "5914175010:AAHGRNHJaeAyZmZNkGGAZRJNi0I28zw8Ebk";
$chat_id = "-893447840";
$arr = array(
  'Имя пользователя: ' => $name,
  'Телефон: ' => $phone,
  'Тема: ' => $header,
  'Сообщение: ' => $message
);

foreach($arr as $key => $value) {
  $txt .= "<b>".$key."</b> ".$value."%0A";
};

$sendToTelegram = fopen("https://api.telegram.org/bot{$token}/sendMessage?chat_id={$chat_id}&parse_mode=html&text={$txt}","r");

if ($sendToTelegram) {
  header('Location: thank-you.html');
} else {
  echo "Error";
}
?>