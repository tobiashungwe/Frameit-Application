import React, { useState } from "react";
import AuthLayout from "../components/Layout/AuthLayout";
import AuthForm from "../components/Auth/AuthForm";
import ErrorSnackbar from "../components/Auth/ErrorSnackbar";
import SuccessSnackbar from "../components/Auth/SuccessSnackbar";
import LinksSection from "../components/Auth/LinksSection";

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
      <AuthForm
        fields={[
          {
            label: "Email or Username",
            value: emailOrUser,
            onChange: (e) => setEmailOrUser(e.target.value),
          },
        ]}
        buttonLabel="Send Reset Instructions"
        onSubmit={handleForgotPassword}
      />

      <LinksSection links={[{ href: "/login", label: "Back to Login" }]} />

      <ErrorSnackbar error={error} onClose={() => setError("")} />
      <SuccessSnackbar success={success} onClose={() => setSuccess("")} />
    </AuthLayout>
  );
};

export default ForgotPasswordPage;
