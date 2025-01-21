import React, { useState } from "react";
import {
  TextField,
  Button,
  Snackbar,
  Link,
  Box,
} from "@mui/material";
import AuthLayout from "../components/Layout/AuthLayout";

const LoginPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    // Basic validation
    if (!username || !password) {
      setError("Please fill out all fields.");
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/api/users/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });
      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || "Login failed");
      }

      const data = await response.json();
      // Typically store token in context or localStorage
      console.log("Access token:", data.access_token);

      setSuccess("Login successful!");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <AuthLayout title="Login">
      <Box component="form" onSubmit={handleLogin}>
        <TextField
          label="Username"
          variant="outlined"
          fullWidth
          margin="normal"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <TextField
          label="Password"
          variant="outlined"
          type="password"
          fullWidth
          margin="normal"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <Button
          type="submit"
          variant="contained"
          color="primary"
          sx={{ mt: 2 }}
          fullWidth
        >
          Login
        </Button>

        <Box sx={{ mt: 2 }}>
          <Link href="/register" underline="hover">
            Don&apos;t have an account? Register
          </Link>
          <br />
          <Link href="/forgot-password" underline="hover">
            Forgot your password?
          </Link>
        </Box>
      </Box>

      <Snackbar
        open={Boolean(error)}
        onClose={() => setError("")}
        message={error}
        autoHideDuration={6000}
      />
      <Snackbar
        open={Boolean(success)}
        onClose={() => setSuccess("")}
        message={success}
        autoHideDuration={6000}
      />
    </AuthLayout>
  );
};

export default LoginPage;