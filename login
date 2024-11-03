<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login System</title>
  <style>
    body,html{
       height: 100px;
       margin:0;
       display: flex;
       justify-content: center;
       align-items: Arial, sans-serif;
       background-color: white;

    }
    .login-container h2{
      margin: 0 0 20px;
    }
    input[type="text"], input[type="password"]{
      width: 100px;
      padding: 10px;
      margin:10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    .login-btn{
      padding: 10px 20px;
      font-size: 16px;
      color:white;
      background-color: #007bff;
      border:none;
      border-radius: 4px;
      cursor: pointer;
      transition: transform 0.4s ease-in-out;
      
    }
    .login-btn:hover{
      transform:translatex(50px);
      background-color: #0056b3;

    }
  </style>
</head>
<body>
  <div class="login-container">
    <h2>login</h2>
    <input type="text" placeholder="Username" required>
    <input type="password" placeholder="password" required>
    <button class="login-btn">Login</button>
  </div>  
</body>
</html>  
