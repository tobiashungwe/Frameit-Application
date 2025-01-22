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

const GroupManagerModal = ({ open, onClose }) => {
  const [groups, setGroups] = useState([]);
  const [newGroupName, setNewGroupName] = useState("");
  const [editGroupId, setEditGroupId] = useState(null);
  const [editGroupName, setEditGroupName] = useState("");

  useEffect(() => {
    if (open) {
      fetchGroups();
    }
  }, [open]);

  const fetchGroups = async () => {
    try {
      const response = await axios.get("/api/groups");
      setGroups(response.data);
    } catch (err) {
      console.error("Failed to fetch groups", err);
    }
  };

  const handleAddGroup = async () => {
    if (!newGroupName.trim()) return;
    try {
      // Using query parameters for name
      const response = await axios.post("/api/groups", null, {
        params: { name: newGroupName },
      });
      setNewGroupName("");
      setGroups([...groups, response.data]);
    } catch (err) {
      console.error("Failed to create group", err);
    }
  };

  const handleEditGroup = (group) => {
    setEditGroupId(group.id);
    setEditGroupName(group.name);
  };

  const handleUpdateGroup = async () => {
    try {
      const response = await axios.put(`/api/groups/${editGroupId}`, null, {
        params: { name: editGroupName },
      });
      setGroups(
        groups.map((g) => (g.id === editGroupId ? response.data : g))
      );
      setEditGroupId(null);
      setEditGroupName("");
    } catch (err) {
      console.error("Failed to update group", err);
    }
  };

  const handleDeleteGroup = async (id) => {
    try {
      await axios.delete(`/api/groups/${id}`);
      setGroups(groups.filter((g) => g.id !== id));
    } catch (err) {
      console.error("Failed to delete group", err);
    }
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      {/* Custom Title with close button */}
      <DialogTitle sx={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <Typography variant="h6">Manage Groups</Typography>
        <IconButton onClick={onClose} size="small">
          <CloseIcon />
        </IconButton>
      </DialogTitle>

      {/* Main Content */}
      <DialogContent dividers>
        {/* Example: if you want a search bar, uncomment below
        <Box sx={{ mb: 2 }}>
          <TextField
            label="Search Groups"
            variant="outlined"
            size="small"
            fullWidth
          />
        </Box>
        */}

        {/* Existing Groups */}
        <Typography variant="subtitle1" sx={{ mb: 1 }}>
          Existing Groups
        </Typography>
        <Paper variant="outlined" sx={{ maxHeight: 200, overflow: "auto", mb: 3 }}>
          <List>
            {groups.map((group) => (
              <ListItem key={group.id} divider>
                {editGroupId === group.id ? (
                  <TextField
                    size="small"
                    value={editGroupName}
                    onChange={(e) => setEditGroupName(e.target.value)}
                    fullWidth
                  />
                ) : (
                  <ListItemText primary={group.name} />
                )}
                <ListItemSecondaryAction>
                  {editGroupId === group.id ? (
                    <IconButton onClick={handleUpdateGroup} edge="end">
                      <EditIcon />
                    </IconButton>
                  ) : (
                    <IconButton onClick={() => handleEditGroup(group)} edge="end">
                      <EditIcon />
                    </IconButton>
                  )}
                  <IconButton onClick={() => handleDeleteGroup(group.id)} edge="end">
                    <DeleteIcon />
                  </IconButton>
                </ListItemSecondaryAction>
              </ListItem>
            ))}
          </List>
        </Paper>

        <Divider sx={{ mb: 2 }} />

        {/* Add New Group */}
        <Typography variant="subtitle1" sx={{ mb: 1 }}>
          Add New Group
        </Typography>
        <Grid container spacing={2}>
          <Grid item xs={12} md={8}>
            <TextField
              label="Group Name"
              value={newGroupName}
              onChange={(e) => setNewGroupName(e.target.value)}
              fullWidth
            />
          </Grid>
          <Grid item xs={12} md={4}>
            <Button
              variant="contained"
              fullWidth
              sx={{ height: "100%" }}
              onClick={handleAddGroup}
            >
              Add
            </Button>
          </Grid>
        </Grid>
      </DialogContent>

      {/* Footer Actions (if needed) */}
      <DialogActions>
        <Button onClick={onClose} color="inherit">
          Close
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default GroupManagerModal;
