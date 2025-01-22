import React, { useEffect, useState } from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  IconButton,
  Button,
  TextField,
  Box,
  Grid,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  Typography,
  Divider,
  Paper,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
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
      <DialogTitle sx={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <Typography variant="h6">Manage Materials</Typography>
        <IconButton onClick={onClose} size="small">
          <CloseIcon />
        </IconButton>
      </DialogTitle>

      <DialogContent dividers>
        {/* Existing Materials */}
        <Typography variant="subtitle1" sx={{ mb: 1 }}>
          Existing Materials
        </Typography>
        <Paper variant="outlined" sx={{ maxHeight: 200, overflow: "auto", mb: 3 }}>
          <List>
            {materials.map((material) => (
              <ListItem key={material.id} divider>
                {editMaterialId === material.id ? (
                  <Box sx={{ display: "flex", flexDirection: "column", width: "100%" }}>
                    <TextField
                      size="small"
                      value={editMaterialName}
                      onChange={(e) => setEditMaterialName(e.target.value)}
                      label="Material Name"
                      sx={{ mb: 1 }}
                    />
                    <TextField
                      size="small"
                      value={editMaterialCategory}
                      onChange={(e) => setEditMaterialCategory(e.target.value)}
                      label="Category"
                    />
                  </Box>
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
        </Paper>

        <Divider sx={{ mb: 2 }} />

        {/* Add New Material */}
        <Typography variant="subtitle1" sx={{ mb: 1 }}>
          Add New Material
        </Typography>
        <Grid container spacing={2}>
          <Grid item xs={12} md={6}>
            <TextField
              label="Material Name"
              value={newMaterialName}
              onChange={(e) => setNewMaterialName(e.target.value)}
              fullWidth
            />
          </Grid>
          <Grid item xs={12} md={6}>
            <TextField
              label="Category"
              value={newMaterialCategory}
              onChange={(e) => setNewMaterialCategory(e.target.value)}
              fullWidth
            />
          </Grid>
          <Grid item xs={12}>
            <Button
              variant="contained"
              onClick={handleAddMaterial}
            >
              Add
            </Button>
          </Grid>
        </Grid>
      </DialogContent>

      <DialogActions>
        <Button onClick={onClose} color="inherit">
          Close
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default MaterialManagerModal;
