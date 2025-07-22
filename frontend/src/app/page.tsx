'use client';

import { useEffect, useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api")
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage("Failed to connect to backend"));
  }, []);

  return (
    <main style={{ display: "flex", minHeight: "100vh", alignItems: "center", justifyContent: "center" }}>
      <h1>{message}</h1>
    </main>
  );
}
