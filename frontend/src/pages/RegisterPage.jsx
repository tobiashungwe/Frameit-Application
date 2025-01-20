import React, { useState } from "react";
import {
  TextField,
  Button,
  Snackbar,
  Link,
  Box,
} from "@mui/material";
import AuthLayout from "../components/Layout/AuthLayout";

const RegisterPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    // Basic validation
    if (!username || !password) {
      setError("Please fill out all fields.");
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/api/users/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });
      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || "Registration failed");
      }

      const data = await response.json();
      setSuccess(data.message || "Registration successful!");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <AuthLayout title="Register">
      <Box component="form" onSubmit={handleRegister}>
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
          color="secondary"
          sx={{ mt: 2 }}
          fullWidth
        >
          Register
        </Button>

        <Box sx={{ mt: 2 }}>
          <Link href="/login" underline="hover">
            Already have an account? Login
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

export default RegisterPage;