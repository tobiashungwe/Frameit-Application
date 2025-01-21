import React, { useState } from "react";
import { TextField, Button, Snackbar, Box, Link } from "@mui/material";
import AuthLayout from "../components/Layout/AuthLayout";

const ForgotPasswordPage = () => {
  const [emailOrUser, setEmailOrUser] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleForgotPassword = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    if (!emailOrUser) {
      setError("Please provide your email or username.");
      return;
    }

    try {
      // Dummy endpoint. Adjust to your actual forgot-password endpoint.
      const response = await fetch("http://localhost:8000/api/users/forgot-password", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email_or_username: emailOrUser }),
      });
      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || "Request failed");
      }

      const data = await response.json();
      setSuccess(data.message || "A reset link has been sent to your email.");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <AuthLayout title="Forgot Password">
      <Box component="form" onSubmit={handleForgotPassword}>
        <TextField
          label="Email or Username"
          variant="outlined"
          fullWidth
          margin="normal"
          value={emailOrUser}
          onChange={(e) => setEmailOrUser(e.target.value)}
        />

        <Button
          type="submit"
          variant="contained"
          color="primary"
          sx={{ mt: 2 }}
          fullWidth
        >
          Send Reset Instructions
        </Button>

        <Box sx={{ mt: 2 }}>
          <Link href="/login" underline="hover">
            Back to Login
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

export default ForgotPasswordPage;