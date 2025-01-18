const useFileUpload = ({ t }) => {
  const handleUploadFile = async (file, setSanitizedContent, setOriginalContent, setIsLoading) => {
    if (!file) {
      alert(t("messages.select_file"));
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setIsLoading(true); 
    try {
      const response = await fetch("http://localhost:8000/api/stories/upload_activity/", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setSanitizedContent(data.sanitized_content);
        setOriginalContent(data.original_content); 
      } else {
        const error = await response.json();
        console.error("File upload error:", error);
        alert(t("messages.upload_error"));
      }
    } catch (error) {
      console.error("Unexpected error during upload:", error);
      alert(t("messages.upload_error"));
    } finally {
      setIsLoading(false); 
    }
  };

  return { handleUploadFile };
};

export default useFileUpload;
