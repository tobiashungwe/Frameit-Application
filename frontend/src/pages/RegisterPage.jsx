import React, { useState } from "react";
import AuthLayout from "../components/Layout/AuthLayout";
import AuthForm from "../components/Auth/AuthForm";
import ErrorSnackbar from "../components/Auth/ErrorSnackbar";
import SuccessSnackbar from "../components/Auth/SuccessSnackbar";
import LinksSection from "../components/Auth/LinksSection";

const RegisterPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

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
        buttonLabel="Register"
        onSubmit={handleRegister}
      />

      <LinksSection links={[{ href: "/login", label: "Already have an account? Login" }]} />

      <ErrorSnackbar error={error} onClose={() => setError("")} />
      <SuccessSnackbar success={success} onClose={() => setSuccess("")} />
    </AuthLayout>
  );
};

export default RegisterPage;
