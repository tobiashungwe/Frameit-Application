import React, { useState } from "react";
import { useNavigate } from "react-router-dom"; // Import the useNavigate hook
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

  const navigate = useNavigate(); // Initialize the navigate function

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

      let data;
      try {
        data = await response.json();
      } catch {
        throw new Error("Invalid response from server");
      }

      if (!response.ok) {
        throw new Error(data.detail || "Login failed");
      }

      // Handle successful login
      setSuccess("Login successful!");
      console.log("Access Token:", data.access_token); // Use as needed

      // Redirect to the homepage
      setTimeout(() => {
        navigate("/"); // Redirect to the homepage after a short delay
      }, 1000); // Delay is optional, used to show the success message briefly
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
