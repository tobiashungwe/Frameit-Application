import React, { useState } from "react";
import AuthLayout from "../components/Layout/AuthLayout";
import AuthForm from "../components/Auth/AuthForm";
import ErrorSnackbar from "../components/Auth/ErrorSnackbar";
import SuccessSnackbar from "../components/Auth/SuccessSnackbar";
import LinksSection from "../components/Auth/LinksSection";
import config from "../config";

const LoginPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    if (!username || !password) {
      setError("Please fill out all fields.");
      return;
    }

    try {
      const response = await fetch(`${config.API_BASE_URL}/api/users/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });
      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || "Login failed");
      }

      const data = await response.json();
      console.log("Access token:", data.access_token);
      setSuccess("Login successful!");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <AuthLayout title="Login">
      <AuthForm
        fields={[
          {
            label: "Username",
            value: username,
            onChange: (e) => setUsername(e.target.value),
          },
          {
            label: "Password",
            type: "password",
            value: password,
            onChange: (e) => setPassword(e.target.value),
          },
        ]}
        buttonLabel="Login"
        onSubmit={handleLogin}
      />

      <LinksSection
        links={[
          { href: "/register", label: "Don't have an account? Register" },
          { href: "/forgot-password", label: "Forgot your password?" },
        ]}
      />

      <ErrorSnackbar error={error} onClose={() => setError("")} />
      <SuccessSnackbar success={success} onClose={() => setSuccess("")} />
    </AuthLayout>
  );
};

export default LoginPage;
