const useFileUpload = ({ t }) => {
  const handleUploadFile = async (file, setSanitizedContent) => {
    if (!file) {
      alert(t("messages.select_file"));
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/api/stories/upload_activity/", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setSanitizedContent(data.sanitized_content);
      } else {
        const error = await response.json();
        console.error("File upload error:", error);
        alert(t("messages.upload_error"));
      }
    } catch (error) {
      console.error("Unexpected error during upload:", error);
      alert(t("messages.upload_error"));
    }
  };

  return { handleUploadFile };
};

export default useFileUpload;
