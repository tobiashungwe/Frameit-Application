const useStoryGeneration = ({ t }) => {
  const handleGenerateStory = async ({
    theme,
    file,
    selectedKeywords,
    content,
    groupCount,
    terrain,
    material,
    language,
    setStory,
    setIsGenerating,
  }) => {
    if (!theme || !file || !groupCount || !terrain || !material || selectedKeywords.length === 0) {
      alert(t("messages.all_fields_required"));
      return;
    }

    setIsGenerating(true);

    try {
      const response = await fetch("http://localhost:8000/api/stories/generate_story", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          theme,
          exercise: { filename: file.name, content: content.data },
          materials: [material],
          terrain,
          selected_keywords: selectedKeywords,
          language,
          group_size: groupCount,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        setStory(data.story);
      } else {
        const errorData = await response.json();
        console.error("Error generating story:", errorData);
        alert(`Error: ${errorData.detail}`);
      }
    } catch (error) {
      console.error("Unexpected error:", error);
      alert(t("messages.error_generating_story"));
    } finally {
      setIsGenerating(false);
    }
  };

  return { handleGenerateStory };
};

export default useStoryGeneration;
