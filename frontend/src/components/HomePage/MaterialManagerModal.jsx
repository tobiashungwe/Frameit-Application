import React, { useEffect, useState } from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField,
  IconButton,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import axios from "axios";

const MaterialManagerModal = ({ open, onClose }) => {
  const [materials, setMaterials] = useState([]);
  const [newMaterialName, setNewMaterialName] = useState("");
  const [newMaterialCategory, setNewMaterialCategory] = useState("");
  const [editMaterialId, setEditMaterialId] = useState(null);
  const [editMaterialName, setEditMaterialName] = useState("");
  const [editMaterialCategory, setEditMaterialCategory] = useState("");

  useEffect(() => {
    if (open) {
      fetchMaterials();
    }
  }, [open]);

  const fetchMaterials = async () => {
    try {
      const response = await axios.get("/api/materials");
      setMaterials(response.data);
    } catch (err) {
      console.error("Failed to fetch materials", err);
    }
  };

  const handleAddMaterial = async () => {
    if (!newMaterialName.trim()) return;
    try {
      // If you're using query params to pass `name` & `category`:
      const response = await axios.post("/api/materials", null, {
        params: {
          name: newMaterialName,
          category: newMaterialCategory,
        },
      });
      setMaterials([...materials, response.data]);
      setNewMaterialName("");
      setNewMaterialCategory("");
    } catch (err) {
      console.error("Failed to create material", err);
    }
  };

  const handleEditMaterial = (material) => {
    setEditMaterialId(material.id);
    setEditMaterialName(material.name);
    setEditMaterialCategory(material.category || "");
  };

  const handleUpdateMaterial = async () => {
    try {
      const response = await axios.put(`/api/materials/${editMaterialId}`, null, {
        params: {
          name: editMaterialName,
          category: editMaterialCategory
        },
      });
      setMaterials(materials.map((m) => (m.id === editMaterialId ? response.data : m)));
      setEditMaterialId(null);
      setEditMaterialName("");
      setEditMaterialCategory("");
    } catch (err) {
      console.error("Failed to update material", err);
    }
  };

  const handleDeleteMaterial = async (id) => {
    try {
      await axios.delete(`/api/materials/${id}`);
      setMaterials(materials.filter((m) => m.id !== id));
    } catch (err) {
      console.error("Failed to delete material", err);
    }
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Manage Materials</DialogTitle>
      <DialogContent dividers>
        {/* Display existing materials */}
        <List>
          {materials.map((material) => (
            <ListItem key={material.id}>
              {editMaterialId === material.id ? (
                <div style={{ display: "flex", flexDirection: "column", width: "100%" }}>
                  <TextField
                    label="Material Name"
                    size="small"
                    value={editMaterialName}
                    onChange={(e) => setEditMaterialName(e.target.value)}
                  />
                  <TextField
                    label="Category"
                    size="small"
                    value={editMaterialCategory}
                    onChange={(e) => setEditMaterialCategory(e.target.value)}
                    sx={{ mt: 1 }}
                  />
                </div>
              ) : (
                <ListItemText
                  primary={material.name}
                  secondary={material.category ? `Category: ${material.category}` : ""}
                />
              )}
              <ListItemSecondaryAction>
                {editMaterialId === material.id ? (
                  <IconButton onClick={handleUpdateMaterial} edge="end">
                    <EditIcon />
                  </IconButton>
                ) : (
                  <IconButton onClick={() => handleEditMaterial(material)} edge="end">
                    <EditIcon />
                  </IconButton>
                )}
                <IconButton onClick={() => handleDeleteMaterial(material.id)} edge="end">
                  <DeleteIcon />
                </IconButton>
              </ListItemSecondaryAction>
            </ListItem>
          ))}
        </List>

        {/* Add new material */}
        <TextField
          label="New Material Name"
          value={newMaterialName}
          onChange={(e) => setNewMaterialName(e.target.value)}
          fullWidth
          margin="dense"
        />
        <TextField
          label="Category (optional)"
          value={newMaterialCategory}
          onChange={(e) => setNewMaterialCategory(e.target.value)}
          fullWidth
          margin="dense"
        />
        <Button variant="contained" onClick={handleAddMaterial} sx={{ mt: 1 }}>
          Add Material
        </Button>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="primary">
          Close
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default MaterialManagerModal;
