# CLAUDE.md - Project Constitution

## Philosophy: Spec-Driven Development

This project follows **Spec-Driven Development (SDD)** principles, where specifications drive implementation, not the other way around.

## Core Principles

### 1. Specification First
- Every feature starts with a clear specification in `/specs`
- Specs define requirements, validation rules, and expected behavior
- Implementation must match specification exactly

### 2. Professional Standards
- Code must be clean, readable, and maintainable
- Proper error handling for all edge cases
- Clear validation messages for user inputs
- Consistent formatting and structure

### 3. Testing & Validation
- All specified features must be implemented
- All validation rules must be enforced
- Error cases must be handled gracefully
- User experience must be smooth and intuitive

### 4. Documentation Excellence
- README.md provides clear usage instructions
- Code includes docstrings for all functions
- Examples demonstrate actual usage
- Instructions are clear for non-technical users

## Project Structure

```
/specs          - Feature specifications and requirements
/src            - Source code implementation
README.md       - User-facing documentation
CLAUDE.md       - This constitution file
```

## Development Workflow

1. **Read the Spec** - Understand requirements in `/specs`
2. **Implement** - Write code that matches spec exactly
3. **Validate** - Ensure all requirements are met
4. **Document** - Update README with usage instructions
5. **Review** - Check against spec before committing

## Quality Checklist

Before considering any phase complete:

- [ ] All spec requirements implemented
- [ ] All validation rules working
- [ ] Error handling for edge cases
- [ ] Clean, readable code
- [ ] Proper documentation
- [ ] Tested manually for user experience

## Version Control

- Commit messages should be clear and descriptive
- Each phase should be a clean, working implementation
- Follow git best practices

---

**Remember**: The spec is the source of truth. Code serves the spec, not vice versa.
